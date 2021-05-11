from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail

from .decorators import record_search_history
from .models import Product, ProductPhoto, Category, Keyword
from account.models import Account
from cart.models import Cart, CartItem
from .filters import ProductNameFilter, KeywordFilter, OrderFilter, CategoryFilter, GetPhotoFilter
from .forms import ContactEmailForm


def index(request):
    top_product_names = ["Cocoa Puffs", "Lucky Charms", "Reese's Puffs", "Fruity Pebbles"]
    top_products = GetPhotoFilter.filter(Product.objects.filter(name__in=top_product_names))

    context = {'top_products': top_products}
    return render(request, 'user/index.html', context)


def about_us_page(request):
    context = {}
    return render(request, 'user/about.html', context)


def contact_us_page(request):
    form = ContactEmailForm()
    if request.method == 'POST':
        form = ContactEmailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                data['name'],
                data['message'],
                data['email'],
                ['shipocereal@gmail.com'],
                fail_silently=False,
            )
        return redirect('home')
    context = {'form': form}
    return render(request, 'user/contact.html', context)


def products_page(request, category):
    """
    Displays product page with all items belonging to supplied category.
    Handles any searches by name
    """
    products = CategoryFilter.filter(category)
    product_filter = ProductNameFilter(request.GET, queryset=products)
    products = product_filter.qs

    # Add photos
    product_list = GetPhotoFilter.filter(products)
    paginator = Paginator(product_list, 8)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)

    context = {'products': product_list, 'product_filter': product_filter}
    return render(request, 'user/products.html', context)


@record_search_history
def product_page(request, product):
    pictures = ProductPhoto.objects.filter(product=product)
    main_picture = pictures[0]
    pictures = pictures[1:]
    if request.method == 'POST':
        # Check if user is logged in
        try:
            account = get_object_or_404(Account, user=request.user)

        # If not get or create an account with the users device uuid
        except TypeError:
            device = request.COOKIES['device']
            account, created = Account.objects.get_or_create(device=device)

        cart = Cart.objects.get(account=account)
        # Check if product is already in cart
        if product in [item.product for item in CartItem.objects.filter(cart=cart)]:
            item = CartItem.objects.get(cart=cart, product=product)
            item.quantity += 1
            item.save()
        else:
            new_cart_item = CartItem.objects.create(cart=cart, product=product)
            new_cart_item.save()
            messages.info(request, f'{product.name} was added to your cart!')
        return redirect('products', 'cereal')

    context = {'product': product, 'pictures': pictures, 'main_picture': main_picture}

    return render(request, 'user/product.html', context)


def get_product_data(request, category):
    """
    Returns a JsonResponse of products split by category and filtered
    by query parameters price, keyword and order
    """
    products = CategoryFilter.filter(category)

    price = request.GET.get('price')
    keyword = request.GET.get('keyword')
    order = request.GET.get('order')

    if price:
        min_max = price.split('-')
        products = products.filter(price__gte=float(min_max[0]),
                                   price__lte=float(min_max[1]))

    if order:
        products = OrderFilter.filter(products, order)

    if keyword:
        products = KeywordFilter.filter(products, keyword)

    # Add photos
    product_list = GetPhotoFilter.filter(products)

    context = {'products': product_list}

    return JsonResponse(context)


def get_keywords(request):
    """ Returns a JsonResponse of all available keywords in the database """
    keywords = Keyword.objects.distinct('name')
    context = {'keywords': [k.name for k in keywords]}
    return JsonResponse(context)

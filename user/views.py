from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404

from .decorators import record_search_history
from .models import Product, ProductPhoto, Category, Keyword
from .filters import ProductNameFilter, KeywordFilter, OrderFilter, CategoryFilter, GetPhotoFilter


def index(request):
    top_product_names = ["Cocoa Puffs", "Lucky Charms", "Reese's Puffs", "Fruity Pebbles"]
    top_products = GetPhotoFilter.filter(Product.objects.filter(name__in=top_product_names))

    context = {'top_products': top_products}
    return render(request, 'user/index.html', context)


def about_us_page(request):
    context = {}
    return render(request, 'user/about.html', context)


def contact_us_page(request):
    context = {}
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

    context = {'products': product_list, 'product_filter': product_filter}
    return render(request, 'user/products.html', context)


@record_search_history
def product_page(request, product):
    pictures = ProductPhoto.objects.filter(product=product)
    main_picture = pictures[0]
    pictures = pictures[1:]

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

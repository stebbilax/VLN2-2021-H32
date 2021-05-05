from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from .models import Product, ProductPhoto, Category
from .decorators import products_page_filter
from .filters import ProductNameFilter


def index(request):
    return render(request, 'user/index.html')


def about_us_page(request):
    return HttpResponse('About us')


def contact_us_page(request):
    return HttpResponse('Contact us')


@products_page_filter
def products_page(request, category):
    """ Displays product page """

    context = {}
    return render(request, 'user/products.html', context)



"""
    # Filter by category
    if category == 'merch':
        cat = Category.objects.get(name='Merch')
        products = Product.objects.filter(category=cat)
    else:
        cat = Category.objects.get(name='Cereal')
        products = Product.objects.filter(category=cat)

    # Order by
    param = request.GET.get('sort')
    if param == 'price_desc':
        products = products.order_by('-price')
    elif param == 'price_asc':
        products = products.order_by('price')
    elif param == 'name_desc':
        products = products.order_by('-name')
    elif param == 'name_asc':
        products = products.order_by('name')

    # Filter product name
    product_filter = ProductNameFilter(request.GET, queryset=products)
    products = product_filter.qs

    # Filter by price

    # Grab product images
    product_list = []
    for prod in products:
        img = ProductPhoto.objects.filter(product=prod)
        if img:
            img = img[0]

        product_list.append({'id': prod.id,
                             'name': prod.name,
                             'price': prod.price,
                             'img': img
                             })

    context = {'products': product_list, 'product_filter': product_filter}
    return render(request, 'user/products.html', context)

"""


def get_product_data(request):
    products = Product.objects.all()
    product_list = []
    for prod in products:
        img = ProductPhoto.objects.filter(product=prod)
        if img:
            img = img[0]

        product_list.append({'id': prod.id,
                             'name': prod.name,
                             'price': prod.price,
                             'img': img.photo.url
                             })

    context = {'products': product_list}

    return JsonResponse(context)
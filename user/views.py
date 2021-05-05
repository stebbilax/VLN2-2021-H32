from django.shortcuts import render, HttpResponse
from .models import Product, ProductPhoto


# Create your views here.
def index(request):
    return render(request, 'user/index.html')


def about_us_page(request):
    return HttpResponse('About us')


def contact_us_page(request):
    return HttpResponse('Contact us')


def products_page(request):
    """ Displays product page """
    products = Product.objects.all()
    product_list = []

    for prod in products:
        img = ProductPhoto.objects.filter(product=prod)
        if img:
            img = img[0]
        else:
            #TODO Change this to some default image
            img = ProductPhoto.objects.filter(product=Product.objects.get(name='DefaultProduct'))[0]

        product_list.append({'id': prod.id,
                             'name': prod.name,
                             'price': prod.price,
                             'img': img
                             })
    print(product_list)


    context = {'products': product_list}
    return render(request, 'user/products.html', context)

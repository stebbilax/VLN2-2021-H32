import django_filters
from django import forms
from django_filters import CharFilter

from .models import Product, Keyword, Category, ProductPhoto


class ProductNameFilter(django_filters.FilterSet):
    """
    Filters the Product model based on a string parameter
    """
    name = CharFilter(field_name='name', lookup_expr='icontains', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'product-search-bar'}))

    class Meta:
        model = Product
        fields = ['name']


class KeywordFilter:
    @staticmethod
    def filter(queryset, keyword):
        """
        Receives a queryset and a keyword string.
        Returns a list of all query objects associated with that keyword
        """
        matches = []
        for el in queryset:
            if Keyword.objects.filter(name=keyword, product=el):
                matches.append(el)

        return matches


class OrderFilter:
    @staticmethod
    def filter(queryset, order):
        """
        Receives a queryset and an order string
        Returns the queryset ordered based on the order string.
        """
        if order == 'price-asc':
            return queryset.order_by('price')
        elif order == 'price-desc':
            return queryset.order_by('-price')
        elif order == 'name-asc':
            return queryset.order_by('name')
        elif order == 'name-desc':
            return queryset.order_by('-name')


class CategoryFilter:
    @staticmethod
    def filter(category):
        """
        Receives a category string as input and queries products accordingly.
        If the string is "merch", returns all merch products
        else returns all cereal products
        """
        if category == 'merch':
            cat = Category.objects.get(name='Merch')
            return Product.objects.filter(category=cat)
        else:
            cat = Category.objects.get(name='Cereal')
            return Product.objects.filter(category=cat)


class GetPhotoFilter:
    @staticmethod
    def filter(queryset):
        """
        Receives  a queryset of products and returns a list of the same objects
        with a corresponding image attached.
        """
        product_list = []
        for prod in queryset:
            try:
                img = ProductPhoto.objects.filter(product=prod)
                if img:
                    img = img[0].photo.url

            except IndexError:
                img = ''

            product_list.append({'id': prod.id,
                                 'name': prod.name,
                                 'price': prod.price,
                                 'img': img
                                 })

        return product_list

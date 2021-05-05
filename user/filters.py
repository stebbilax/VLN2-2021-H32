import django_filters
from django_filters import RangeFilter, CharFilter

from .models import Product


class ProductNameFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name']


class ProductPriceFilter(django_filters.FilterSet):
    price = RangeFilter()

    class Meta:
        model = Product
        fields = ['price']


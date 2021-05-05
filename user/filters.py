import django_filters
from django_filters import RangeFilter, CharFilter

from .models import Product, Keyword


class ProductNameFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name']


class KeywordFilter:

    @staticmethod
    def filter(querySet, keyword):
        to_be_deleted = []
        for el in querySet:
            if not Keyword.objects.filter(name=keyword, product=el):
                to_be_deleted.append(el.id)

        querySet.filter(id__in=to_be_deleted).delete()
        print(querySet)
        return querySet
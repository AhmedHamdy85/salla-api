import django_filters
from .models import Product
class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model= Product
        fields = {
            'name': ['icontains'],
            'category': ['exact'],
            'price': ['exact', 'gte', 'lte'],
        }
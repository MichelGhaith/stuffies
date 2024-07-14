import django_filters
from .models import Product
from django.db.models import Q
class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    brand = django_filters.CharFilter(field_name='brand__name', lookup_expr='iexact')
    product_type = django_filters.CharFilter(field_name='product_type__name', lookup_expr='iexact')
    material = django_filters.CharFilter(field_name='material__name', lookup_expr='iexact')
    fit = django_filters.CharFilter(field_name='fit__name', lookup_expr='iexact')
    name_and_description = django_filters.CharFilter(method='filter_by_name_and_description')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'brand', 'product_type','material','fit','name_and_description']
    
    def filter_by_name_and_description(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(description__icontains=value)
        )
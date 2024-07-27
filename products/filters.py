from django_filters import rest_framework as filters
from .models import Product
from django.db.models import Q

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    brand = filters.CharFilter(field_name='brand__name', lookup_expr='iexact')
    product_type = filters.CharFilter(field_name='product_type__name', lookup_expr='iexact')
    material = filters.CharFilter(field_name='material__name', lookup_expr='iexact')
    fit = filters.CharFilter(field_name='fit__name', lookup_expr='iexact')
    name_and_description = filters.CharFilter(method='filter_by_name_and_description', label= 'name and description')
    size = filters.CharFilter(field_name='size_color_quantities__size__name',label = 'size', lookup_expr='iexact')
    color = filters.CharFilter(field_name='size_color_quantities__color__name',label = 'color' ,lookup_expr='iexact')
    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'brand', 'product_type','material','fit','name_and_description','size','color']
    
    def filter_by_name_and_description(self, queryset,_, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(description__icontains=value)
        ).distinct()
        
    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.distinct()
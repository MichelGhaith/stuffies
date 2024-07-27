from django.shortcuts import render
from .models import Product,ProductSizeColorQuantity,Review,ProductColorImages
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from .filters import ProductFilter
from django.db.models import Prefetch

# Create your views here.

class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.select_related('brand', 'product_type', 'material', 'fit').prefetch_related(
        Prefetch('size_color_quantities', queryset=ProductSizeColorQuantity.objects.select_related('color', 'size').all()),
        Prefetch('product_review', queryset= Review.objects.all(),),
        Prefetch('product_color_images', queryset= ProductColorImages.objects.select_related('color').prefetch_related('images').all())
        ).all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    
from django.shortcuts import render
from .models import Product
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from .filters import ProductFilter
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('brand', 'product_type', 'material', 'fit').all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
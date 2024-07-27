from rest_framework import serializers
from . import models
from django.shortcuts import get_object_or_404
from django.db.models import Sum,Avg

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = ['name'] 
        
class ProductSizeColorQuantitySerializer(serializers.ModelSerializer):
    color = serializers.StringRelatedField()
    size = serializers.StringRelatedField()

    class Meta:
        model = models.ProductSizeColorQuantity
        fields = ['color', 'size', 'quantity', 'price']
        
class ProductSerializer(serializers.ModelSerializer):
    
    brand = serializers.StringRelatedField() 
    product_type = serializers.StringRelatedField()
    material = serializers.StringRelatedField()
    fit = serializers.StringRelatedField()
    colors_with_quantities = serializers.SerializerMethodField()
    sizes_with_quantities = serializers.SerializerMethodField()
    colors_with_sizes_quantities = serializers.SerializerMethodField()
    stock_status = serializers.SerializerMethodField() 
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    
    class Meta:
        model = models.Product
        fields = fields = ['name','description','brand','product_type','material','fit','price','quantity',
                           'stock_status','average_rating','review_count','created_at',
                           'colors_with_sizes_quantities','colors_with_quantities','sizes_with_quantities']
        
    def get_colors_with_quantities(self, obj):
        color_quantities = {}
        for item in obj.size_color_quantities.all():
            color_name = item.color.name
            color_quantities[color_name] = color_quantities.get(color_name, 0) + item.quantity
        return [{'color': color, 'quantity': quantity} for color, quantity in color_quantities.items()]
    
    def get_sizes_with_quantities(self, obj):
        size_quantities = {}
        for item in obj.size_color_quantities.all():
            size_name = item.size.name
            size_quantities[size_name] = size_quantities.get(size_name, 0) + item.quantity
        return [{'size': size, 'quantity': quantity} for size, quantity in size_quantities.items()]
    
    def get_colors_with_sizes_quantities(self, obj):
        colors = {}
        for item in obj.size_color_quantities.all():
            color_name = item.color.name
            size_name = item.size.name
            if color_name not in colors:
                colors[color_name] = {}
            colors[color_name][size_name] = colors[color_name].get(size_name, 0) + item.quantity
        return [{'color': color, 'sizes_with_quantities': [{'size': size, 'quantity': quantity} for size, quantity in sizes.items()]} for color, sizes in colors.items()]
    
    def get_stock_status(self, obj):
        return 'In Stock' if obj.quantity > 0 else 'Out of Stock'

    def get_average_rating(self, obj):
        avg_rating = obj.product_review.aggregate(average= Avg('rating', default=0))['average']
        return avg_rating

    def get_review_count(self, obj):
        return obj.product_review.count()
    




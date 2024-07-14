from rest_framework import serializers
from .models import Product
from django.shortcuts import get_object_or_404
class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField() 
    product_type = serializers.StringRelatedField()
    material = serializers.StringRelatedField()
    fit = serializers.StringRelatedField()
    
    class Meta:
        model = Product
        fields = '__all__'
        
    
    def create(self, validated_data):
        brand_name = validated_data.pop('brand')
        product_type_name = validated_data.pop('product_type')
        material_name = validated_data.pop('material')
        fit_name = validated_data.pop('fit')

        brand = get_object_or_404(Brand, name=brand_name)
        product_type = get_object_or_404(Type, name=product_type_name)
        material = get_object_or_404(Material, name=material_name)
        fit = get_object_or_404(Fit, name=fit_name)

        product = Product.objects.create(
            brand=brand, product_type=product_type, material=material, fit=fit, **validated_data)
        return product

    def update(self, instance, validated_data):
        brand_name = validated_data.pop('brand')
        product_type_name = validated_data.pop('product_type')
        material_name = validated_data.pop('material')
        fit_name = validated_data.pop('fit')

        instance.brand = get_object_or_404(Brand, name=brand_name)
        instance.product_type = get_object_or_404(Type, name=product_type_name)
        instance.material = get_object_or_404(Material, name=material_name)
        instance.fit = get_object_or_404(Fit, name=fit_name)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
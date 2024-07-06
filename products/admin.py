from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Brand)
admin.site.register(models.Type)
admin.site.register(models.Fit)
admin.site.register(models.Material)
admin.site.register(models.Image)
admin.site.register(models.Product)
admin.site.register(models.ProductColorImages)
admin.site.register(models.ProductSizeColorQuantity)
admin.site.register(models.Color)
admin.site.register(models.Size)
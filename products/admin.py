from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Brand)
admin.site.register(models.Type)
admin.site.register(models.Fit)
admin.site.register(models.Material)
admin.site.register(models.Product)
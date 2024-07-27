from django.contrib import admin
from . import models
# Register your models here.
#@admin.register(models.ProductSizeColorQuantity)
#class ProductSizeColorQuantityAdmin(admin.ModelAdmin):
#    def save_model(self, request, obj, form, change):
#        if change:
#            update_fields = []
#            for field in form.changed_data:
#                update_fields.append(field)
#            if update_fields:
#                obj.save(update_fields=update_fields)
#            else:
#                obj.save()
#        else:
#            obj.save()
#        super().save_model(request, obj, form, change)

class ProductSizeColorQuantityInline(admin.TabularInline):
    model = models.ProductSizeColorQuantity
    extra = 1
        
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('quantity',)
    inlines = [ProductSizeColorQuantityInline,]

admin.site.register(models.Brand)
admin.site.register(models.Type)
admin.site.register(models.Fit)
admin.site.register(models.Material)
admin.site.register(models.Color)
admin.site.register(models.Size)
admin.site.register(models.Review)
from django.db import models
from django.utils import timezone
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length= 50, null= False,  unique= True)
    def __str__(self):
        return self.name
    
class Type(models.Model):
    name = models.CharField(max_length= 50, null= False, unique= True)
    def __str__(self):
        return self.name
    
class Material(models.Model):
    name = models.CharField(max_length= 50, null= False, unique= True)
    def __str__(self):
        return self.name
    
class Fit(models.Model):
    name = models.CharField(max_length= 50, null= False, unique= True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length= 250, null= False, default= '')
    description = models.CharField(max_length= 250, null= True)
    quantity = models.IntegerField(null= False, default= 0)
    price = models.IntegerField(null= False, default= 0)
    created_at = models.DateField(null= False, default= timezone.now)
    brand = models.ForeignKey(Brand, on_delete= models.PROTECT, null= True)
    product_type = models.ForeignKey(Type, on_delete= models.PROTECT, null= False)
    material = models.ForeignKey(Material, on_delete= models.PROTECT, null= False)
    fit = models.ForeignKey(Fit, on_delete= models.PROTECT, null= False) 
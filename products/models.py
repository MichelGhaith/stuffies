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

class Color(models.Model):
    name = models.CharField(max_length= 50, null= False, unique= True)
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length= 50, null= False, unique= True)
    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length= 100, null= True, blank= True)
    image = models.ImageField(upload_to = 'images')
    
    def __str__(self):
        return self.title if self.title else 'No title available'

class Product(models.Model):
    name = models.CharField(max_length= 250, null= False, default= '')
    description = models.CharField(max_length= 250, null= True, blank= True)
    quantity = models.PositiveIntegerField(null= False, default= 0)
    price = models.PositiveIntegerField(null= False, default= 0)
    created_at = models.DateField(null= False, default= timezone.now)
    brand = models.ForeignKey(Brand, on_delete= models.PROTECT, null= True, blank= True)
    product_type = models.ForeignKey(Type, on_delete= models.PROTECT, null= False)
    material = models.ForeignKey(Material, on_delete= models.PROTECT, null= False)
    fit = models.ForeignKey(Fit, on_delete= models.PROTECT, null= False) 
    
    def __str__(self):
        return self.name 
    

class Product_Color_Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color , on_delete=models.PROTECT)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default= 0, null= False)
    price = models.PositiveIntegerField(default= 0, null= False)

    def __str__(self):
        return str(self.product) + " " + str(self.color) + ' ' + str(self.size)
    
class Product_Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color , on_delete=models.PROTECT)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.product) + " " + str(self.color)
    
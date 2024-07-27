from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from . import models

@receiver(post_save, sender=models.ProductSizeColorQuantity)
def add_a_product(sender, instance, created, **kwargs):
    print("instance")
    print(instance)
    print("created")
    print(created)
    print("kwargs")
    print(kwargs)
    pass
        
# Generated by Django 5.0.6 on 2024-07-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_image_productcolorimages_delete_productcolorimage'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='productcolorimages',
            constraint=models.UniqueConstraint(fields=('product', 'color'), name='unique_product_color'),
        ),
        migrations.AddConstraint(
            model_name='productsizecolorquantity',
            constraint=models.UniqueConstraint(fields=('product', 'color', 'size'), name='unique_product_color_size'),
        ),
    ]
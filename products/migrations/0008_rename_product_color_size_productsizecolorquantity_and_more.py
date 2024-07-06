# Generated by Django 5.0.6 on 2024-07-06 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_image_title_alter_product_brand_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_Color_Size',
            new_name='ProductSizeColorQuantity',
        ),
        migrations.RemoveField(
            model_name='product_color',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product_color',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product_color',
            name='product',
        ),
        migrations.CreateModel(
            name='ProductColorImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Product_Color',
        ),
    ]

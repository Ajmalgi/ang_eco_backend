# Generated by Django 4.1.6 on 2023-02-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_products_product_image_products_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]

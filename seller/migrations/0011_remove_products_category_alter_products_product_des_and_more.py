# Generated by Django 4.1.6 on 2023-02-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0010_products_seller_alter_products_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.AlterField(
            model_name='products',
            name='product_des',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]

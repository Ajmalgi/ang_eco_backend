# Generated by Django 4.1.6 on 2023-02-12 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_seller_seller_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_pic',
            field=models.ImageField(blank=True, null=True, upload_to='seller/'),
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-12 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_remove_seller_seller_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='seller_pic',
            field=models.ImageField(default='', upload_to='seller/'),
        ),
    ]
# Generated by Django 2.2.6 on 2020-05-26 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_products'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bags',
        ),
        migrations.DeleteModel(
            name='Clothing',
        ),
        migrations.DeleteModel(
            name='Footwear',
        ),
    ]

# Generated by Django 2.2.6 on 2020-05-04 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('brand_title', models.CharField(max_length=100)),
                ('item_details', models.TextField(max_length=1000)),
                ('size', models.CharField(choices=[('m', 'M'), ('sm', 'SM'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')], default='m', max_length=20)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=20)),
                ('category', models.CharField(choices=[('shirt', 'shirt'), ('t-shirt', 't-shirt'), ('jeans', 'jeans'), ('trousers', 'trousers')], default='shirt', max_length=20)),
                ('price', models.FloatField()),
                ('is_published', models.BooleanField(default='False')),
            ],
        ),
    ]

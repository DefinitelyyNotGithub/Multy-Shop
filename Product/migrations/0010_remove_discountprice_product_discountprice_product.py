# Generated by Django 5.0.3 on 2024-06-29 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_productmodel_color_productmodel_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discountprice',
            name='product',
        ),
        migrations.AddField(
            model_name='discountprice',
            name='product',
            field=models.ManyToManyField(related_name='Discount', to='Product.productmodel'),
        ),
    ]

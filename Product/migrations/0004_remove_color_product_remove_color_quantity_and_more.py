# Generated by Django 5.0.3 on 2024-04-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_remove_color_product_color_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='product',
        ),
        migrations.RemoveField(
            model_name='color',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='size',
            name='product',
        ),
        migrations.RemoveField(
            model_name='size',
            name='quantity',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='color',
            field=models.ManyToManyField(related_name='color', to='Product.color'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='size',
            field=models.ManyToManyField(related_name='size', to='Product.size'),
        ),
    ]

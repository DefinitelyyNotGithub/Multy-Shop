# Generated by Django 5.0.3 on 2024-07-28 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0041_alter_recentlyviewedproducts_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentlyviewedproducts',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

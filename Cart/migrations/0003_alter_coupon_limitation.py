# Generated by Django 5.0.3 on 2024-08-26 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0002_alter_orderedproduct_options_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='limitation',
            field=models.PositiveSmallIntegerField(default=10000),
        ),
    ]

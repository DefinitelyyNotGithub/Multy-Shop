# Generated by Django 5.0.3 on 2024-09-14 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0004_remove_coupon_apply_to_total_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='discount_mount',
            new_name='discount_amount',
        ),
    ]

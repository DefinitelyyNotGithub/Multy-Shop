# Generated by Django 5.0.3 on 2024-07-28 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0042_alter_recentlyviewedproducts_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recentlyviewedproducts',
            old_name='data',
            new_name='date',
        ),
    ]

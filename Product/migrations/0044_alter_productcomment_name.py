# Generated by Django 5.0.3 on 2024-07-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0043_rename_data_recentlyviewedproducts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

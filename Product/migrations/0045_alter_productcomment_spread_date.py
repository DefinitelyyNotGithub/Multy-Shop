# Generated by Django 5.0.3 on 2024-07-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0044_alter_productcomment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='spread_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-07-29 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0052_productmodel_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]

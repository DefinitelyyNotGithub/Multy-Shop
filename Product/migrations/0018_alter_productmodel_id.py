# Generated by Django 5.0.3 on 2024-07-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0017_alter_productmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-07-03 12:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0015_alter_productmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True, verbose_name=uuid.uuid4),
        ),
    ]

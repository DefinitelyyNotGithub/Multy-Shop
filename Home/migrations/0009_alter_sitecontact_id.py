# Generated by Django 5.0.3 on 2024-08-08 10:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_alter_sitecontact_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitecontact',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True, verbose_name=uuid.UUID('778fc6de-07ad-4265-879b-5837d1abd040')),
        ),
    ]

# Generated by Django 5.0.3 on 2024-08-07 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_userextrainfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('zip_code', models.CharField(max_length=30)),
            ],
        ),
    ]

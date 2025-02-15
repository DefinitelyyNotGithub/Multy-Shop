# Generated by Django 5.0.3 on 2024-04-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField()),
                ('seen', models.BooleanField(default=False, verbose_name='MARK AS SEEN')),
            ],
            options={
                'verbose_name': 'User message',
                'verbose_name_plural': 'User messages',
            },
        ),
    ]

# Generated by Django 5.0.3 on 2024-05-09 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_aboutus_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus_model',
            name='A_1_body',
        ),
        migrations.RemoveField(
            model_name='aboutus_model',
            name='A_1_title',
        ),
        migrations.RemoveField(
            model_name='aboutus_model',
            name='A_2_body',
        ),
        migrations.RemoveField(
            model_name='aboutus_model',
            name='A_2_title',
        ),
        migrations.RemoveField(
            model_name='aboutus_model',
            name='B_1_body',
        ),
        migrations.RemoveField(
            model_name='aboutus_model',
            name='B_1_title',
        ),
        migrations.RemoveField(
            model_name='aboutus_model',
            name='B_2_body',
        ),
        migrations.RemoveField(
            model_name='aboutus_model',
            name='B_2_title',
        ),
        migrations.RemoveField(
            model_name='aboutus_model',
            name='B_3_body',
        ),
        migrations.RemoveField(
            model_name='aboutus_model',
            name='B_3_title',
        ),
        migrations.AddField(
            model_name='aboutus_model',
            name='title',
            field=models.CharField(default='TITLE', max_length=100),
        ),
    ]

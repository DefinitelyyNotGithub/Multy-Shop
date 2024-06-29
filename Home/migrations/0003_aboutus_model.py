# Generated by Django 5.0.3 on 2024-05-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_sitecontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pottage', models.ImageField(blank=True, null=True, upload_to='images/aboutus_title')),
                ('general_description', models.TextField(verbose_name='General description')),
                ('A_1_title', models.CharField(blank=True, max_length=30, null=True, verbose_name='first Paragraph title')),
                ('A_1_body', models.TextField(blank=True, null=True, verbose_name='first Paragraph')),
                ('A_2_title', models.CharField(blank=True, max_length=30, null=True, verbose_name='second paragraph title')),
                ('A_2_body', models.TextField(blank=True, null=True, verbose_name='second paragraph')),
                ('B_1_title', models.CharField(blank=True, max_length=25, null=True, verbose_name='small paragraph title 1')),
                ('B_1_body', models.TextField(blank=True, null=True, verbose_name='small paragraph 1')),
                ('B_2_title', models.CharField(blank=True, max_length=25, null=True, verbose_name='small paragraph title 2')),
                ('B_2_body', models.TextField(blank=True, null=True, verbose_name='small paragraph 2')),
                ('B_3_title', models.CharField(blank=True, max_length=25, null=True, verbose_name='small paragraph title 3')),
                ('B_3_body', models.TextField(blank=True, null=True, verbose_name='small paragraph 3')),
            ],
            options={
                'verbose_name': 'about us page',
            },
        ),
    ]

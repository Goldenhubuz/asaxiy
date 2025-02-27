# Generated by Django 5.1.6 on 2025-02-24 10:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=130, null=True, unique=True)),
                ('model', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('main_image', models.ImageField(upload_to='images/product_detail')),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('like', models.PositiveIntegerField(default=0)),
                ('availability', models.BooleanField(default=True)),
                ('installment', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Big Product',
                'verbose_name_plural': 'Big Products',
                'db_table': 'big_products',
            },
        ),
    ]

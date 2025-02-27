# Generated by Django 5.1.6 on 2025-02-24 10:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=130, null=True, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/news/')),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'db_table': 'news',
            },
        ),
    ]

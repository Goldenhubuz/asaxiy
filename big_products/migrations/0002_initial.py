# Generated by Django 5.1.6 on 2025-02-24 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('big_products', '0001_initial'),
        ('details', '0002_initial'),
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigproductmodel',
            name='book',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shared.bookmodel'),
        ),
        migrations.AddField(
            model_name='bigproductmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.categorymodel'),
        ),
        migrations.AddField(
            model_name='bigproductmodel',
            name='prod',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shared.productmodel'),
        ),
    ]

# Generated by Django 5.1.6 on 2025-02-24 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('big_products', '0001_initial'),
        ('details', '0001_initial'),
        ('eav', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteristicsmodel',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eav.attribute'),
        ),
        migrations.AddField(
            model_name='characteristicsmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='big_products.bigproductmodel'),
        ),
        migrations.AddField(
            model_name='discountmodel',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='big_products.bigproductmodel'),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='big_products.bigproductmodel'),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='big_products.bigproductmodel'),
        ),
    ]

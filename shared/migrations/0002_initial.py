# Generated by Django 5.1.6 on 2025-02-24 10:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('big_products', '0002_initial'),
        ('shared', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='big_products.bigproductmodel'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deliverymodel',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shared.ordermodel'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.brandmodel'),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.publishermodel'),
        ),
        migrations.AddField(
            model_name='wishlistmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='big_products.bigproductmodel'),
        ),
        migrations.AddField(
            model_name='wishlistmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

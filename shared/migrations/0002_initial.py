# Generated by Django 4.2.3 on 2023-07-22 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('big_products', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.brandmodel'),
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
            model_name='cartmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='big_products.bigproductmodel'),
        ),
        migrations.AddField(
            model_name='cartmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.authormodel'),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.publishermodel'),
        ),
    ]

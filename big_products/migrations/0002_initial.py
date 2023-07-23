# Generated by Django 4.2.3 on 2023-07-22 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('big_products', '0001_initial'),
        ('shared', '0001_initial'),
        ('details', '0001_initial'),
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

# Generated by Django 4.2.3 on 2023-07-22 06:56

from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('big_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=50, unique=True)),
                ('pages', models.PositiveSmallIntegerField(blank=True, default=1)),
                ('cover', models.CharField(choices=[('soft', 'Мягкая'), ('hard', 'Твёрдая'), ('softwithslipcase', 'Мягкая + Футляр')], default='soft', max_length=20)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('logo', models.ImageField(upload_to='images/brand/')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
                'db_table': 'carts',
            },
        ),
        migrations.CreateModel(
            name='DeliveryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('cost', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Delivery',
                'verbose_name_plural': 'Deliveries',
                'db_table': 'deliveries',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('summary', models.PositiveIntegerField()),
                ('status', models.CharField(blank=True, choices=[('wait', 'Ожидание'), ('cancel', 'Отменено'), ('success', 'Успешно')], default='wait', max_length=10, null=True)),
                ('address', models.CharField(max_length=255)),
                ('index_p', models.PositiveIntegerField(blank=True, null=True)),
                ('paid', models.PositiveIntegerField(blank=True, null=True)),
                ('rem_sum', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='PickupLocationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('target', models.CharField(max_length=255)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('weekend', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Pickup Location',
                'verbose_name_plural': 'Pickup Locations',
                'db_table': 'pickup_locations',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='PublisherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
                'db_table': 'publishers',
            },
        ),
        migrations.CreateModel(
            name='WishlistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='big_products.bigproductmodel')),
            ],
            options={
                'verbose_name': 'Wishlist',
                'verbose_name_plural': 'Wishlists',
                'db_table': 'wishlists',
            },
        ),
    ]

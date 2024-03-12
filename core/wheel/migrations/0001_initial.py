# Generated by Django 5.0.2 on 2024-03-12 09:24

import django.db.models.deletion
import wheel.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='categories/')),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(choices=[(12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')])),
                ('width', models.IntegerField(blank=True)),
                ('length', models.IntegerField(blank=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('month_3_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('month_6_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('month_9_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('passport_image', models.FileField(blank=True, null=True, upload_to=wheel.models.order_image_path)),
                ('longitude', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=100)),
                ('is_checked', models.BooleanField(default=False)),
                ('details', models.ManyToManyField(blank=True, related_name='orders', to='wheel.detail')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('climate', models.IntegerField(blank=True, choices=[(1, 'Летние'), (2, 'Зимние'), (3, 'Универсальный')], null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wheels', to='wheel.category')),
                ('details', models.ManyToManyField(blank=True, related_name='wheels', to='wheel.detail')),
            ],
        ),
        migrations.AddField(
            model_name='detail',
            name='wheel',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='wheel.wheel'),
        ),
        migrations.CreateModel(
            name='WheelImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='wheels/')),
                ('wheel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wheel.wheel')),
            ],
        ),
        migrations.AddField(
            model_name='wheel',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='wheel_images', to='wheel.wheelimages'),
        ),
    ]

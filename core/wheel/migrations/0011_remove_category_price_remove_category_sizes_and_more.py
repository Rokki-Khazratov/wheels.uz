# Generated by Django 5.0.2 on 2024-02-22 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheel', '0010_remove_wheel_price_remove_wheel_size_category_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='price',
        ),
        migrations.RemoveField(
            model_name='category',
            name='sizes',
        ),
        migrations.AddField(
            model_name='size',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wheel.wheel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='size',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
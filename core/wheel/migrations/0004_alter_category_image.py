# Generated by Django 5.0.2 on 2024-02-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheel', '0003_alter_wheel_price_alter_wheelimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='categories/'),
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheel', '0006_remove_order_wheels_order_details_order_is_checked_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
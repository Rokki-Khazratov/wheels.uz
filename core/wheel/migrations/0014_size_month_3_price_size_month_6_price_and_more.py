# Generated by Django 5.0.2 on 2024-02-23 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheel', '0013_remove_wheel_details_remove_wheel_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='month_3_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='size',
            name='month_6_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='size',
            name='month_9_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

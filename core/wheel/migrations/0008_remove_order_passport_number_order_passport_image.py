# Generated by Django 5.0.2 on 2024-02-28 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheel', '0007_alter_order_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='passport_number',
        ),
        migrations.AddField(
            model_name='order',
            name='passport_image',
            field=models.FileField(blank=True, null=True, upload_to='passport_images/'),
        ),
    ]
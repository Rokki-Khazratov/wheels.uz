# Generated by Django 5.0.2 on 2024-02-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='lenght',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='detail',
            name='width',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheel', '0004_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='wheel',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='wheel_images', to='wheel.wheelimages'),
        ),
        migrations.AlterField(
            model_name='wheel',
            name='climate',
            field=models.IntegerField(choices=[(1, 'Летние'), (2, 'Зимние')]),
        ),
        migrations.AlterField(
            model_name='wheel',
            name='size',
            field=models.IntegerField(choices=[(13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')]),
        ),
        migrations.AlterField(
            model_name='wheelimages',
            name='image',
            field=models.ImageField(upload_to='wheels/'),
        ),
    ]
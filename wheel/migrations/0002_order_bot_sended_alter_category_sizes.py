# Generated by Django 5.0.2 on 2024-04-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bot_sended',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='wheel.categorysizes'),
        ),
    ]
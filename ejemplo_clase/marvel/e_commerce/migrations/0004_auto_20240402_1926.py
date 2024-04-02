# Generated by Django 3.2.2 on 2024-04-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0003_auto_20240402_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='bought_qty',
            field=models.PositiveIntegerField(default=0, verbose_name='bought_qty'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wished_qty',
            field=models.PositiveIntegerField(default=0, verbose_name='wished_qty'),
        ),
    ]
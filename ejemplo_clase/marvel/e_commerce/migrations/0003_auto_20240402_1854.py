# Generated by Django 3.2.2 on 2024-04-02 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0002_wishlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name': 'Whishlist', 'verbose_name_plural': 'Whishlist_comics'},
        ),
        migrations.AlterModelTable(
            name='wishlist',
            table='Whishlist_comics',
        ),
    ]
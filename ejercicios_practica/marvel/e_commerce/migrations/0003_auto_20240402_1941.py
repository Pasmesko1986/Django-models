# Generated by Django 3.2.2 on 2024-04-02 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e_commerce', '0002_wishlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name': 'Whishlist', 'verbose_name_plural': 'Whishlist_comics'},
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='bought_qty',
            field=models.PositiveIntegerField(default=0, verbose_name='bought_qty'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='cart',
            field=models.PositiveIntegerField(default=0, verbose_name='cart'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='comic',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.comic', verbose_name='Comic'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='favorite',
            field=models.CharField(default='', max_length=120, verbose_name='Favorite'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wished_qty',
            field=models.PositiveIntegerField(default=0, verbose_name='wished_qty'),
        ),
        migrations.AlterModelTable(
            name='wishlist',
            table='Whishlist_comics',
        ),
    ]

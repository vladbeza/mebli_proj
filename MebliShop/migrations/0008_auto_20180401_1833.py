# Generated by Django 2.0.2 on 2018-04-01 18:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MebliShop', '0007_auto_20180325_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pub_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.FloatField(null=True),
        ),
    ]

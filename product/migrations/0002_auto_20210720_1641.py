# Generated by Django 3.2.5 on 2021-07-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='buy_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sell_price',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-19 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20210720_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
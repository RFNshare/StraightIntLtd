# Generated by Django 3.2.5 on 2021-07-16 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20210716_2215'),
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Car',
            new_name='Invoice',
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-16 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_merge_20210714_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='uid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

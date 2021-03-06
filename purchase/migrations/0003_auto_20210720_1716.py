# Generated by Django 3.2.5 on 2021-07-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_alter_purchase_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='details',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='products',
        ),
        migrations.AddField(
            model_name='purchase',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_no',
            field=models.IntegerField(null=True),
        ),
    ]

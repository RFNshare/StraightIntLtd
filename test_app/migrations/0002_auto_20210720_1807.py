# Generated by Django 3.2.5 on 2021-07-20 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyCustomModal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_app.country')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='fleet',
            name='car',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Fleet',
        ),
        migrations.AddField(
            model_name='mycustommodal',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_app.state'),
        ),
    ]
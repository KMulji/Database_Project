# Generated by Django 3.2.8 on 2021-11-27 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_alter_order_dateplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
    ]
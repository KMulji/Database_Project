# Generated by Django 3.2.8 on 2021-11-07 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_customer_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='PhoneNumber',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='PhoneNumber',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
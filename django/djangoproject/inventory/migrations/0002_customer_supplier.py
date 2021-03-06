# Generated by Django 3.2.8 on 2021-11-07 17:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('Email', models.EmailField(max_length=70)),
                ('Address', models.CharField(max_length=100)),
                ('PhoneNumber', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('Email', models.EmailField(max_length=70)),
                ('Address', models.CharField(max_length=100)),
                ('PhoneNumber', models.CharField(max_length=100)),
            ],
        ),
    ]

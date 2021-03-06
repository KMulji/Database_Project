# Generated by Django 3.2.8 on 2021-11-07 17:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20211107_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('DatePlaced', models.DateTimeField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.customer')),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-29 18:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.room')),
            ],
        ),
        migrations.CreateModel(
            name='Enrolled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.CharField(max_length=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='university.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='university.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]

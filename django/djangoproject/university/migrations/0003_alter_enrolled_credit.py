# Generated by Django 3.2.8 on 2021-10-31 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_course_enrolled_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolled',
            name='credit',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]

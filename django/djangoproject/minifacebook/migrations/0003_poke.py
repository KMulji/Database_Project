# Generated by Django 3.2.8 on 2021-10-23 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minifacebook', '0002_alter_status_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('pokee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poke_pokee', to='minifacebook.profile')),
                ('poker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poke_poker', to='minifacebook.profile')),
            ],
        ),
    ]

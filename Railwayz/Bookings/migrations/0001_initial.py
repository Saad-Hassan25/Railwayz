# Generated by Django 5.0.3 on 2024-03-23 20:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Trains', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_station', models.CharField(max_length=100)),
                ('destination_station', models.CharField(max_length=100)),
                ('journey_date', models.DateField()),
                ('class_type', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trains.train')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

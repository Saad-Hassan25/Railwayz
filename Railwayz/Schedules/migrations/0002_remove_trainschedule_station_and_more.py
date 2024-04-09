# Generated by Django 5.0.3 on 2024-04-08 21:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schedules', '0001_initial'),
        ('Stations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainschedule',
            name='station',
        ),
        migrations.AddField(
            model_name='trainschedule',
            name='ArrivalStation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='arrival_schedule', to='Stations.station'),
        ),
        migrations.AddField(
            model_name='trainschedule',
            name='DepartureStation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='departure_schedules', to='Stations.station'),
        ),
    ]

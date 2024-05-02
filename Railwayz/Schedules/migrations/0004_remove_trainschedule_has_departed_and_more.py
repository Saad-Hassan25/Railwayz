# Generated by Django 5.0.3 on 2024-04-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schedules', '0003_trainschedule_has_departed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainschedule',
            name='has_departed',
        ),
        migrations.AddField(
            model_name='trainschedule',
            name='departure_status',
            field=models.CharField(choices=[('No', 'NotDeparted'), ('Yes', 'Departed'), ('Cancelled', 'Cancelled'), ('Delayed', 'Delayed')], default='No', max_length=10),
        ),
    ]

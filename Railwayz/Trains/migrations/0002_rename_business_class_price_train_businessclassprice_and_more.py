# Generated by Django 5.0.3 on 2024-03-23 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trains', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='train',
            old_name='business_class_price',
            new_name='businessClassPrice',
        ),
        migrations.RenameField(
            model_name='train',
            old_name='economy_class_price',
            new_name='economyClassPrice',
        ),
    ]

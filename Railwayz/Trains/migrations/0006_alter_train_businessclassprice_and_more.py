# Generated by Django 5.0.3 on 2024-04-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trains', '0005_alter_train_businessclassprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='businessClassPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='train',
            name='economyClassPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

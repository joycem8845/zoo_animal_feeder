# Generated by Django 2.1.2 on 2018-10-11 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_animal_feeders', '0005_auto_20181011_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='breakfast',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='dinner',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='lunch',
            field=models.TimeField(default='00:00'),
        ),
    ]
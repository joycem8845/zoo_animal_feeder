# Generated by Django 2.1.2 on 2018-10-11 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_animal_feeders', '0003_auto_20181011_0212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animaltype',
            old_name='animal_type',
            new_name='a_type',
        ),
    ]
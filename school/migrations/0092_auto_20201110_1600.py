# Generated by Django 3.1.2 on 2020-11-10 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0091_auto_20201110_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deposit',
            old_name='modeofreturn',
            new_name='modeofdeposit',
        ),
    ]

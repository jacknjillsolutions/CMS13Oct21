# Generated by Django 3.1.3 on 2021-05-20 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0291_logdokqc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logdokqc',
            old_name='create',
            new_name='icreate',
        ),
        migrations.RenameField(
            model_name='logdokqc',
            old_name='updatee',
            new_name='iupdatee',
        ),
    ]

# Generated by Django 3.0.4 on 2021-07-11 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0358_emsplanttype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emsplanttype',
            old_name='Desc',
            new_name='Descr',
        ),
    ]

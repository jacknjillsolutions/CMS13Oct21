# Generated by Django 3.2 on 2021-10-05 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0410_auto_20211005_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisor1',
            name='datefrom',
        ),
        migrations.RemoveField(
            model_name='supervisor1',
            name='dateto',
        ),
    ]

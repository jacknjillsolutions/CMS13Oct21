# Generated by Django 3.2 on 2021-08-06 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0397_auto_20210806_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rpt_emssumth',
            name='LivSum',
        ),
        migrations.RemoveField(
            model_name='rpt_emssumth',
            name='TeraceCnt',
        ),
    ]

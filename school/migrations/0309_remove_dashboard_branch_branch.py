# Generated by Django 3.2 on 2021-06-05 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0308_auto_20210605_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard_branch',
            name='branch',
        ),
    ]

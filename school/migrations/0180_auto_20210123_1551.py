# Generated by Django 3.1.2 on 2021-01-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0179_auto_20210123_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='Route_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='code',
            field=models.IntegerField(unique=True),
        ),
    ]

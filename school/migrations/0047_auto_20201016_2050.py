# Generated by Django 3.1.2 on 2020-10-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0046_auto_20201016_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_data',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='daily_data',
            name='comm',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='daily_data',
            name='pel',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='daily_data',
            name='tsrate',
            field=models.FloatField(default=0.0),
        ),
    ]
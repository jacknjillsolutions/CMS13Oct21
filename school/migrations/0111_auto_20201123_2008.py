# Generated by Django 3.1.3 on 2020-11-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0110_auto_20201123_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_data',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

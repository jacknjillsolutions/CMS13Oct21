# Generated by Django 3.0.4 on 2020-09-29 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_supervisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='active',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.1.4 on 2021-01-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0191_auto_20210125_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisor',
            name='Route_attached1',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
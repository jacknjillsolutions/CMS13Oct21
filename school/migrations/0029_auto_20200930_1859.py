# Generated by Django 3.0.4 on 2020-09-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0028_auto_20200930_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cowmilkrates',
            name='deduction_calculation',
            field=models.FloatField(default=0.0),
        ),
    ]

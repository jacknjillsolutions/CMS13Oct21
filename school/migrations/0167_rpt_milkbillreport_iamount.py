# Generated by Django 3.1.2 on 2021-01-19 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0166_rpt_milkbillreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_milkbillreport',
            name='iamount',
            field=models.FloatField(default=0.0),
        ),
    ]

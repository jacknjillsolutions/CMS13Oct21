# Generated by Django 3.2 on 2021-08-06 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0394_rpt_emssumthonly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rpt_emssumth',
            name='cid',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
    ]

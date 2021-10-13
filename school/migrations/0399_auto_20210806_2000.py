# Generated by Django 3.2 on 2021-08-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0398_auto_20210806_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_emssumth',
            name='girth',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_emssumth',
            name='height',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_emssumth',
            name='leaves',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_emssumth',
            name='teraceCnt',
            field=models.IntegerField(blank=True, default=0.0, null=True),
        ),
    ]
# Generated by Django 3.2 on 2021-06-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0314_auto_20210617_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloan',
            name='Flat',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='cloan',
            name='billing',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
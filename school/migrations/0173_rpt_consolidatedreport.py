# Generated by Django 3.1.4 on 2021-01-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0172_auto_20210121_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='RPT_consolidatedreport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('Shift', models.CharField(max_length=255)),
                ('routecode', models.CharField(blank=True, max_length=255, null=True)),
                ('centercode', models.CharField(max_length=255)),
                ('Milktype', models.CharField(max_length=255)),
                ('kgs', models.FloatField(default=0.0)),
                ('Ltrs', models.FloatField(default=0.0)),
                ('afat', models.FloatField(default=0.0)),
                ('asnf', models.FloatField(default=0.0)),
                ('Fat', models.FloatField(default=0.0)),
                ('Snf', models.FloatField(default=0.0)),
                ('RateLTR', models.FloatField(default=0.0)),
                ('pel', models.FloatField(default=0.0)),
                ('gamount', models.FloatField(default=0.0)),
            ],
        ),
    ]
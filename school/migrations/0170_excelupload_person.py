# Generated by Django 3.1.4 on 2021-01-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0169_auto_20210120_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excelupload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('Shift', models.CharField(max_length=255, null=True)),
                ('Milktype', models.CharField(max_length=255, null=True)),
                ('kgs', models.FloatField(default=0.0, null=True)),
                ('Ltrs', models.FloatField(default=0.0, null=True)),
                ('Fat', models.FloatField(default=0.0, null=True)),
                ('Snf', models.FloatField(default=0.0, null=True)),
                ('RateLTR', models.FloatField(default=0.0, null=True)),
                ('Netamount', models.FloatField(default=0.0, null=True)),
                ('PiExp', models.FloatField(default=0.0, null=True)),
                ('Total', models.FloatField(default=0.0, null=True)),
                ('accholdername', models.CharField(blank=True, max_length=255, null=True)),
                ('routename', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('Shift', models.CharField(max_length=255, null=True)),
                ('Milktype', models.CharField(max_length=255, null=True)),
                ('kgs', models.FloatField(default=0.0, null=True)),
                ('Ltrs', models.FloatField(default=0.0, null=True)),
                ('Fat', models.FloatField(default=0.0, null=True)),
                ('Snf', models.FloatField(default=0.0, null=True)),
                ('RateLTR', models.FloatField(default=0.0, null=True)),
                ('Netamount', models.FloatField(default=0.0, null=True)),
                ('PiExp', models.FloatField(default=0.0, null=True)),
                ('Total', models.FloatField(default=0.0, null=True)),
                ('accholdername', models.CharField(blank=True, max_length=255, null=True)),
                ('routename', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]

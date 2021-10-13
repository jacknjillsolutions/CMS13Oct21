# Generated by Django 3.1.2 on 2021-04-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0272_rpt_excel_bankwise'),
    ]

    operations = [
        migrations.CreateModel(
            name='RPT_Centerwisesreport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(blank=True, max_length=255, null=True)),
                ('routecode', models.CharField(blank=True, max_length=255, null=True)),
                ('centercode', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('shift', models.CharField(blank=True, max_length=255, null=True)),
                ('milk_type', models.CharField(blank=True, max_length=255, null=True)),
                ('fat', models.FloatField(blank=True, default=0.0, null=True)),
                ('snf', models.FloatField(blank=True, default=0.0, null=True)),
                ('routename', models.CharField(blank=True, max_length=255, null=True)),
                ('centername', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('ltrrate', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
    ]
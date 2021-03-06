# Generated by Django 3.1.4 on 2021-04-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0281_rpt_consolidated_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='rpt_dailydata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(blank=True, max_length=255, null=True)),
                ('routecode', models.CharField(blank=True, max_length=255, null=True)),
                ('centercode', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('shift', models.CharField(blank=True, max_length=255, null=True)),
                ('sampno', models.IntegerField(default=0)),
                ('sampno2', models.IntegerField(default=0)),
                ('milk_type', models.CharField(blank=True, max_length=255, null=True)),
                ('can', models.FloatField(blank=True, default=0.0, null=True)),
                ('qty', models.FloatField(blank=True, default=0.0, null=True)),
                ('ltrs', models.FloatField(blank=True, default=0.0, null=True)),
                ('fat', models.FloatField(blank=True, default=0.0, null=True)),
                ('snf', models.FloatField(blank=True, default=0.0, null=True)),
                ('clr', models.FloatField(blank=True, default=0.0, null=True)),
                ('tsrate', models.FloatField(blank=True, default=0.0, null=True)),
                ('comm', models.FloatField(blank=True, default=0.0, null=True)),
                ('pel', models.FloatField(blank=True, default=0.0, null=True)),
                ('amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('ltrrate', models.FloatField(blank=True, default=0.0, null=True)),
                ('ltrtsrate', models.FloatField(blank=True, default=0.0, null=True)),
                ('net', models.FloatField(blank=True, default=0.0, null=True)),
                ('routename', models.CharField(blank=True, max_length=255, null=True)),
                ('centername', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]

# Generated by Django 3.1.2 on 2021-02-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0247_auto_20210225_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='RPT_Daywiseabstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('centercode', models.CharField(max_length=255)),
                ('Milktype', models.CharField(max_length=255)),
                ('kgs', models.FloatField(blank=True, default=0.0, null=True)),
                ('Ltrs', models.FloatField(blank=True, default=0.0, null=True)),
                ('fatkgs', models.FloatField(blank=True, default=0.0, null=True)),
                ('snfkgs', models.FloatField(blank=True, default=0.0, null=True)),
                ('Fat', models.FloatField(blank=True, default=0.0, null=True)),
                ('Snf', models.FloatField(blank=True, default=0.0, null=True)),
                ('Snf1', models.FloatField(blank=True, default=0.0, null=True)),
                ('comm', models.FloatField(blank=True, default=0.0, null=True)),
                ('cartage', models.FloatField(blank=True, default=0.0, null=True)),
                ('incentive', models.FloatField(blank=True, default=0.0, null=True)),
                ('net', models.FloatField(blank=True, default=0.0, null=True)),
                ('rate', models.FloatField(blank=True, default=0.0, null=True)),
                ('gamount', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
    ]

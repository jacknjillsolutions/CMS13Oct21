# Generated by Django 3.0.4 on 2020-10-09 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0035_auto_20201009_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cowmilkcategory',
            name='commission',
        ),
        migrations.RemoveField(
            model_name='cowmilkcategory',
            name='max_SNF',
        ),
        migrations.RemoveField(
            model_name='cowmilkcategory',
            name='max_fat',
        ),
        migrations.RemoveField(
            model_name='cowmilkcategory',
            name='min_SNF',
        ),
        migrations.RemoveField(
            model_name='cowmilkcategory',
            name='min_fat',
        ),
        migrations.RemoveField(
            model_name='cowmilkcategory',
            name='rate',
        ),
    ]
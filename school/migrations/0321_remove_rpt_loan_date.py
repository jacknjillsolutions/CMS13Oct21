# Generated by Django 3.2 on 2021-06-18 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0320_rpt_loan_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rpt_loan',
            name='date',
        ),
    ]

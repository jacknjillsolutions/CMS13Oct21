# Generated by Django 3.2 on 2021-06-18 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0324_remove_rpt_loan_closingdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rpt_loan',
            name='date',
        ),
    ]

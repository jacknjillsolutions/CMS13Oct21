# Generated by Django 3.2 on 2021-06-19 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0337_rename_principal_amt_rpt_loan_installment_principle_amt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rpt_loan',
            old_name='installment_principle_amt',
            new_name='principal_amt',
        ),
    ]

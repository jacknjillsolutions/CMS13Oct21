# Generated by Django 3.1.2 on 2020-11-02 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0074_auto_20201102_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deposit',
            old_name='loanno',
            new_name='loan_no',
        ),
    ]
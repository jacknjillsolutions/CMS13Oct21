# Generated by Django 3.1.2 on 2020-11-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0075_auto_20201102_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='refund',
            name='loan_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
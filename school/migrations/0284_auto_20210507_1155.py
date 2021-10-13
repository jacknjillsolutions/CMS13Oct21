# Generated by Django 3.1.2 on 2021-05-07 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0283_auto_20210430_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_consolidatedreport',
            name='branch',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rpt_consolidatedreport',
            name='centername',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rpt_consolidatedreport',
            name='net',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_consolidatedreport',
            name='routename',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rpt_consolidatedreport',
            name='tsrate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='rpt_consolidatedreport',
            name='centercode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rpt_excel_bankwise',
            name='amount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='rpt_excel_bankwise',
            name='total',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
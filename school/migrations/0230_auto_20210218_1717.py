# Generated by Django 3.1.2 on 2021-02-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0229_auto_20210218_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='aarrears',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='acentercode',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='adate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='aothers',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='autofine',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='cartage',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='cattlefeed',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='commission',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='emtcharges',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='insurance',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='medicine',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='rarrears',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='rothers',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='seed',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='stationary',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='rpt_milkbillvoucher',
            name='stores',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='aarrears',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='aothers',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='autofine',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='cartage',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='cattlefeed',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='centercode',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='commission',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='emtcharges',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='insurance',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='medicine',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='rarrears',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='rothers',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='seed',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='stationary',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='additions',
            name='stores',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
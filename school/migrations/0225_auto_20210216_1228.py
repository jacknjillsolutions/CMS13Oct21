# Generated by Django 3.1.2 on 2021-02-16 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0224_auto_20210215_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloan',
            name='installment_amt',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cloan',
            name='interest_amt',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='rpt_milkbillvoucher',
            name='installment_amt',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='rpt_milkbillvoucher',
            name='interest_amt',
            field=models.FloatField(default=0.0),
        ),
    ]

# Generated by Django 3.0.4 on 2020-09-30 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0023_remove_cowmilkrates_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cowmilkrates',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='commission',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='commission_type',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='curd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='deduction_calculation',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='fat_from',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='fat_to',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='fixed_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='max_SNF',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='max_fat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='min_SNF',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='min_fat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='min_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='penalty_in_RS',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='premium',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='sour_milk',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cowmilkrates',
            name='sour_milkrate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
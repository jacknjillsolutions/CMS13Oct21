# Generated by Django 3.0.4 on 2021-07-10 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0354_auto_20210709_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMSData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaCode', models.CharField(blank=True, max_length=10, null=True)),
                ('blkCode', models.CharField(blank=True, max_length=10, null=True)),
                ('teraceNo', models.CharField(blank=True, max_length=10, null=True)),
                ('treeNo', models.IntegerField(blank=True, null=True)),
                ('plantDate', models.DateField(blank=True, null=True)),
                ('plantType', models.CharField(blank=True, max_length=10, null=True)),
                ('height', models.FloatField(blank=True, default=0.0, null=True)),
                ('girth', models.FloatField(blank=True, default=0.0, null=True)),
                ('leaveCnt', models.IntegerField(blank=True, null=True)),
                ('tcWeeType', models.CharField(blank=True, max_length=10, null=True)),
                ('tcWaterlog', models.CharField(blank=True, max_length=10, null=True)),
                ('tcMud', models.CharField(blank=True, max_length=10, null=True)),
                ('TCNet', models.CharField(blank=True, max_length=10, null=True)),
                ('WTRing', models.CharField(blank=True, max_length=10, null=True)),
                ('Waterpipe', models.CharField(blank=True, max_length=10, null=True)),
                ('PnDFung', models.CharField(blank=True, max_length=10, null=True)),
                ('PNDTermite', models.CharField(blank=True, max_length=10, null=True)),
                ('PNDChType', models.CharField(blank=True, max_length=10, null=True)),
                ('PNDDate', models.DateField(blank=True, null=True)),
                ('manurFType', models.CharField(blank=True, max_length=10, null=True)),
                ('ManureRate', models.FloatField(blank=True, default=0.0, null=True)),
                ('ManureDate', models.DateField(blank=True, null=True)),
                ('Remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('extdate', models.DateField(blank=True, null=True)),
                ('extUser', models.CharField(blank=True, max_length=255)),
                ('fileName', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]

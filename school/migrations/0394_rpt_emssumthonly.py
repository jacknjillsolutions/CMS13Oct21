# Generated by Django 3.2 on 2021-08-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0393_auto_20210806_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='rpt_emsSumTHOnly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaCode', models.CharField(blank=True, max_length=10, null=True)),
                ('blkCode', models.CharField(blank=True, max_length=10, null=True)),
                ('teraceNo', models.CharField(blank=True, max_length=10, null=True)),
                ('treeCnt', models.IntegerField(blank=True, default=0.0, null=True)),
                ('aHeight', models.FloatField(blank=True, default=0.0, null=True)),
                ('aGirth', models.FloatField(blank=True, default=0.0, null=True)),
                ('aLeaves', models.FloatField(blank=True, default=0.0, null=True)),
                ('eid', models.IntegerField(blank=True, default=0.0, null=True)),
            ],
        ),
    ]

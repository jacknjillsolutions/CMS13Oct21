# Generated by Django 3.1.2 on 2021-01-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0175_auto_20210122_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='referralcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

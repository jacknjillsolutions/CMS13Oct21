# Generated by Django 3.0.4 on 2020-09-29 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_auto_20200929_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='Route_number',
            field=models.IntegerField(),
        ),
    ]
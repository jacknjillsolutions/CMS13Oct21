# Generated by Django 3.2 on 2021-06-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0345_alter_dailydataexcelupload_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailydataexcelupload',
            name='file_name',
            field=models.CharField(max_length=12),
        ),
    ]

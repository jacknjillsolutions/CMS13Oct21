# Generated by Django 3.1.2 on 2020-11-25 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0118_auto_20201125_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='center',
            old_name='agent_name',
            new_name='BM_Cartage_unit',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='bm',
            new_name='BM_Comm_unit',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='bm_amount',
            new_name='BM_comm_amount',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='bm_cartage',
            new_name='BankBranch',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='cm_cartage_amount',
            new_name='CM_Cartage_amount',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='branch',
            new_name='CM_Cartage_unit',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='cm',
            new_name='CM_Comm_unit',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='cm_amount',
            new_name='CM_comm_amount',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='kilo',
            new_name='Distance',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='document',
            new_name='Document',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='cm_cartage',
            new_name='Formula',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='ifsc',
            new_name='agentcode',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='state',
            new_name='ifsccode',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='route_number',
            new_name='routecode',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='supervisor',
            new_name='supervisorcode',
        ),
        migrations.RenameField(
            model_name='center',
            old_name='village_name',
            new_name='villagecode',
        ),
    ]

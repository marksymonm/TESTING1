# Generated by Django 5.1.1 on 2024-12-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUPCLaboratoryEquipment', '0014_alter_borrowing_records_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentaccounts',
            name='confirmation_token',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True),
        ),
    ]
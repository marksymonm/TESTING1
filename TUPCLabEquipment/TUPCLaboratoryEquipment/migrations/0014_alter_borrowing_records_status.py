# Generated by Django 5.1.1 on 2024-11-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUPCLaboratoryEquipment', '0013_alter_borrowing_records_items_borrowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowing_records',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Handed In', 'Handed In'), ('Returned', 'Returned'), ('Overdue', 'Overdue')], default='Pending', max_length=10),
        ),
    ]
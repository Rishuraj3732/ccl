# Generated by Django 4.2 on 2023-05-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0018_remove_vehicle_booking_statement_bill_no'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BTH_details',
            new_name='Vehical_Expenses',
        ),
        migrations.AlterField(
            model_name='vehicle_booking_statement',
            name='month',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

# Generated by Django 4.2 on 2023-06-08 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0031_outstanding_consignor_outstanding_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outstanding',
            name='id',
        ),
        migrations.AlterField(
            model_name='outstanding',
            name='Bill_SubOn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='outstanding',
            name='Date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='outstanding',
            name='LR_No',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='outstanding',
            name='Received_on_dt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

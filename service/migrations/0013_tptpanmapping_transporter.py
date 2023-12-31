# Generated by Django 4.2 on 2023-05-27 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_vehicle_booking_statement_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='TptPanMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpt_name', models.CharField(max_length=255, unique=True)),
                ('pan', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpt', models.CharField(max_length=255)),
                ('tds_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('actual_freight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tds_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tds', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tds_form', models.CharField(max_length=10)),
                ('tds_exempt', models.CharField(max_length=3)),
                ('neft_date', models.DateField()),
                ('tpt_pan_mapping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.tptpanmapping')),
            ],
        ),
    ]

# Generated by Django 5.2.2 on 2025-07-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_hourlyusage_delete_electricityusage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('consumption_kwh', models.FloatField()),
            ],
            options={
                'ordering': ['year', 'month'],
                'unique_together': {('year', 'month')},
            },
        ),
        migrations.DeleteModel(
            name='HourlyUsage',
        ),
    ]

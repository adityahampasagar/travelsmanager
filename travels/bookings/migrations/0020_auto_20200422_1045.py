# Generated by Django 3.0.4 on 2020-04-22 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20200416_1959'),
        ('bookings', '0019_auto_20200422_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer'),
        ),
    ]

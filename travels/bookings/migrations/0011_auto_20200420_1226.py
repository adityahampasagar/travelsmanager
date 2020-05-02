# Generated by Django 3.0.4 on 2020-04-20 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20200416_1959'),
        ('bookings', '0010_auto_20200420_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer'),
        ),
    ]

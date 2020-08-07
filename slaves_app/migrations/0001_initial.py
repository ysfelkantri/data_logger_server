# Generated by Django 2.2.15 on 2020-08-07 15:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemoryZoneOfSlaves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_registers_address', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=50)),
                ('value_class', models.CharField(choices=[('FLOAT32', 'REAL (FLOAT32)'), ('FLOAT32', 'SINGLE (FLOAT32)'), ('FLOAT32', 'FLOAT32'), ('UNIXTIMEF32', 'UNIXTIMEF32'), ('FLOAT64', 'LREAL (FLOAT64)'), ('FLOAT64', 'FLOAT  (FLOAT64)'), ('FLOAT64', 'DOUBLE (FLOAT64)'), ('FLOAT64', 'FLOAT64'), ('UNIXTIMEF64', 'UNIXTIMEF64'), ('INT64', 'INT64'), ('UINT64', 'UINT64'), ('UNIXTIMEI64', 'UNIXTIMEI64'), ('UNIXTIMEI32', 'UNIXTIMEI32'), ('INT32', 'INT32'), ('UINT32', 'DWORD (UINT32)'), ('UINT32', 'UINT32'), ('INT16', 'INT (INT16)'), ('INT16', 'INT16'), ('UINT16', 'WORD (UINT16)'), ('UINT16', 'UINT (UINT16)'), ('UINT16', 'UINT16'), ('BOOLEAN', 'BOOL (BOOLEAN)'), ('BOOLEAN', 'BOOLEAN'), ('STRING', 'STRING')], default='INT16', max_length=15, verbose_name='value_class')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baudrate', models.CharField(choices=[('9600', '9600'), ('19200', '19200'), ('38400', '38400')], max_length=10)),
                ('parity', models.CharField(choices=[('E', 'Even'), ('N', 'None'), ('O', 'Odd'), (0, 'default')], max_length=5)),
                ('stop', models.PositiveSmallIntegerField(default=1)),
                ('bits', models.PositiveSmallIntegerField(default=8)),
            ],
        ),
        migrations.CreateModel(
            name='Slave',
            fields=[
                ('slave_address', models.IntegerField(default=0, primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(247), django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=100)),
                ('enable', models.BooleanField(default=True)),
                ('mac', models.CharField(max_length=50)),
                ('setting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='slaves_app.Setting')),
            ],
        ),
        migrations.CreateModel(
            name='SensorValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_picking', models.DateTimeField(auto_now_add=True, null=True)),
                ('memory_zone_of_slaves', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slaves_app.MemoryZoneOfSlaves')),
            ],
        ),
        migrations.AddField(
            model_name='memoryzoneofslaves',
            name='slave',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='slaves_app.Slave'),
        ),
    ]

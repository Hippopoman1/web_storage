# Generated by Django 5.1.3 on 2024-12-19 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stor',
            fields=[
                ('equipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='equipment_images/')),
                ('location', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=128)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('employee', 'Employee')], default='employee', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('return_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('employee_id', models.ForeignKey(limit_choices_to={'role': 'employee'}, on_delete=django.db.models.deletion.CASCADE, to='storage.user')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('employee_id', models.ForeignKey(limit_choices_to={'role': 'employee'}, on_delete=django.db.models.deletion.CASCADE, to='storage.user')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=50)),
                ('equipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.stor')),
                ('admin_id', models.ForeignKey(limit_choices_to={'role': 'admin'}, on_delete=django.db.models.deletion.CASCADE, to='storage.user')),
            ],
        ),
    ]
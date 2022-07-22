# Generated by Django 4.0.6 on 2022-07-22 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('vehicle_number', models.CharField(max_length=25, unique=True)),
                ('model_number', models.CharField(max_length=25)),
                ('capacity', models.PositiveSmallIntegerField()),
                ('color', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images/')),
                ('monthly_rent', models.PositiveIntegerField()),
                ('v_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='vehicles.vehicleprovider')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('other', 'other')], max_length=10)),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('direction', models.CharField(choices=[('One-Side', 'One-Side'), ('Both-Side', 'Both-Side')], max_length=10)),
                ('fix_rent', models.PositiveIntegerField(default=0)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passengers', to='vehicles.vehicle')),
            ],
        ),
    ]

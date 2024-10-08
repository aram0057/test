# Generated by Django 5.1 on 2024-09-09 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('plant_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('scientific_name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('flowering_category', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('maintenance_type', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('photo_url', models.URLField(max_length=255)),
                ('watering_needs', models.CharField(max_length=255)),
                ('sunlight_needs', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Plants',
            },
        ),
        migrations.CreateModel(
            name='Plant_Needs',
            fields=[
                ('need_id', models.IntegerField(primary_key=True, serialize=False)),
                ('watering_schedule', models.CharField(max_length=255)),
                ('soil_type', models.CharField(max_length=255)),
                ('fertilizer', models.CharField(max_length=255)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.plant')),
            ],
            options={
                'db_table': 'Plant_Needs',
            },
        ),
    ]

# Generated by Django 4.2.5 on 2024-08-31 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('centre_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
            options={
                'db_table': 'Centre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MelbourneSuburbs',
            fields=[
                ('postcode', models.IntegerField(primary_key=True, serialize=False)),
                ('suburb', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Melbourne_suburbs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Waste',
            fields=[
                ('waste_id', models.IntegerField(primary_key=True, serialize=False)),
                ('waste_type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Waste',
                'managed': False,
            },
        ),
    ]

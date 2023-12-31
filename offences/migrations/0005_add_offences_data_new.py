# Generated by Django 4.2.4 on 2023-10-06 23:50

from django.db import migrations

def insert_offences_data(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Offence = apps.get_model('offences', 'Offence')
    
    offences_data = [
        {'id': 1, 'offence_description': 'Speeding', 'offence_max_fine': 1000, 'offence_max_points': 3},
        {'id': 2, 'offence_description': 'Speeding on a motorway', 'offence_max_fine': 2500, 'offence_max_points': 6},
        {'id': 3, 'offence_description': 'Seat belt offence', 'offence_max_fine': 500, 'offence_max_points': 0},
        {'id': 4, 'offence_description': 'Illegal parking', 'offence_max_fine': 500, 'offence_max_points': 0},
        {'id': 5, 'offence_description': 'Drink driving', 'offence_max_fine': 10000, 'offence_max_points': 11},
        {'id': 6, 'offence_description': 'Driving without a licence', 'offence_max_fine': 10000, 'offence_max_points': 0},
        {'id': 7, 'offence_description': 'Driving without a licence', 'offence_max_fine': 10000, 'offence_max_points': 0},
        {'id': 8, 'offence_description': 'Traffic light offences', 'offence_max_fine': 1000, 'offence_max_points': 3},
        {'id': 9, 'offence_description': 'Cycling on pavement', 'offence_max_fine': 500, 'offence_max_points': 0},
        {'id': 10, 'offence_description': 'Failure to have control of vehicle', 'offence_max_fine': 1000, 'offence_max_points': 3},
        {'id': 11, 'offence_description': 'Dangerous driving', 'offence_max_fine': 1000, 'offence_max_points': 11},
        {'id': 12, 'offence_description': 'Careless driving', 'offence_max_fine': 5000, 'offence_max_points': 6},
        {'id': 13, 'offence_description': 'Dangerous cycling', 'offence_max_fine': 2500, 'offence_max_points': 0},
    ]

    for data in offences_data:
        Offence.objects.using(db_alias).create(**data)


class Migration(migrations.Migration):

    dependencies = [
        ('offences', '0004_rename_incident_id_fine_incident'),
    ]

    operations = [
        migrations.RunPython(insert_offences_data, migrations.RunPython.noop),
    ]

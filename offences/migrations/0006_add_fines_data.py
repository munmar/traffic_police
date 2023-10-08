# Generated by Django 4.2.4 on 2023-10-07 16:35

from django.db import migrations

def insert_fines_data(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Fine = apps.get_model('offences', 'Fine')
    
    fines_data = [
        {'id': 1, 'fine_amount': 2000, 'fine_points': 6, 'incident_id': 3},
        {'id': 2, 'fine_amount': 50, 'fine_points': 0, 'incident_id': 2},
        {'id': 3, 'fine_amount': 500, 'fine_points': 3, 'incident_id': 4},
    ]

    for data in fines_data:
        Fine.objects.using(db_alias).create(**data)


class Migration(migrations.Migration):

    dependencies = [
        ('offences', '0005_add_offences_data_new'),
        ('reports', '0002_add_incidents_data'),
    ]

    operations = [
        migrations.RunPython(insert_fines_data, migrations.RunPython.noop),
    ]

# Generated by Django 4.2.4 on 2023-10-06 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offences', '0003_add_offence_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fine',
            old_name='incident_id',
            new_name='incident',
        ),
    ]
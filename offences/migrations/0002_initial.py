# Generated by Django 4.2.5 on 2023-10-06 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reports', '0001_initial'),
        ('offences', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fine',
            name='incident_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.incident'),
        ),
    ]
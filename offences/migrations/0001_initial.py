# Generated by Django 4.2.5 on 2023-10-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fine_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fine_points', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Offence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offence_description', models.TextField()),
                ('offence_max_fine', models.DecimalField(decimal_places=2, max_digits=10)),
                ('offence_max_points', models.PositiveIntegerField()),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-14 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musician',
            old_name='Instrument_type',
            new_name='instrument_type',
        ),
    ]

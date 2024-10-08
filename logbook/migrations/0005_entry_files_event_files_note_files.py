# Generated by Django 4.2.1 on 2024-08-21 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0004_entry_minimized'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='files',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='event',
            name='files',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='note',
            name='files',
            field=models.JSONField(default=list),
        ),
    ]

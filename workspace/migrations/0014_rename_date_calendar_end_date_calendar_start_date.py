# Generated by Django 4.2.4 on 2023-08-31 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0013_calendar_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendar',
            old_name='date',
            new_name='end_date',
        ),
        migrations.AddField(
            model_name='calendar',
            name='start_date',
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
    ]

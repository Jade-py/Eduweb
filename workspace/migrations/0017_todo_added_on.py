# Generated by Django 4.2.4 on 2023-09-18 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0016_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='added_on',
            field=models.DateField(default=datetime.date(2023, 9, 18)),
        ),
    ]

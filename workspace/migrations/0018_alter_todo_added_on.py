# Generated by Django 4.2.4 on 2023-09-19 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0017_todo_added_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_on',
            field=models.DateField(default=datetime.date(2023, 9, 19)),
        ),
    ]

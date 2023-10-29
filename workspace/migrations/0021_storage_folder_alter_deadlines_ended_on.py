# Generated by Django 4.2.4 on 2023-09-25 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0020_remove_todo_added_on_deadlines'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage',
            name='folder',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='deadlines',
            name='ended_on',
            field=models.DateField(default=datetime.date(2023, 9, 25)),
        ),
    ]

# Generated by Django 4.2.1 on 2023-11-01 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayTracker', '0003_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='date',
            field=models.DateField(null=True, verbose_name=datetime.date(2023, 11, 1)),
        ),
    ]
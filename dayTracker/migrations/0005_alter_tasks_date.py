# Generated by Django 4.2.1 on 2023-11-03 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayTracker', '0004_tasks_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
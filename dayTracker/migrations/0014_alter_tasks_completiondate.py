# Generated by Django 4.2.1 on 2023-11-24 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayTracker', '0013_alter_tasks_completiondate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='completionDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-29 14:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("calory_counter", "0004_exercise"),
    ]

    operations = [
        migrations.RenameField(
            model_name="exercise",
            old_name="time",
            new_name="time_hour",
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_postexercise_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='total_calorie_exercise',
            field=models.FloatField(default=0, null=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-05 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calory_counter', '0016_remove_receipe_food_sel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='recipe',
        ),
    ]
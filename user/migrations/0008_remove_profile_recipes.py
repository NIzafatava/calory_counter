# Generated by Django 4.2.4 on 2023-09-05 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_profile_recipes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='recipes',
        ),
    ]
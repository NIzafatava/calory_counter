# Generated by Django 4.2.4 on 2023-08-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "calory_counter",
            "0009_receipe_carbohydrate_receipe_difficulty_level_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipe",
            name="img_url",
            field=models.TextField(blank=True, null=True),
        ),
    ]

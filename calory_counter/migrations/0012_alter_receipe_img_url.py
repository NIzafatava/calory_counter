# Generated by Django 4.2.4 on 2023-08-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calory_counter", "0011_receipe_ingredients"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipe",
            name="img_url",
            field=models.ImageField(null=True, upload_to="static/recipes"),
        ),
    ]

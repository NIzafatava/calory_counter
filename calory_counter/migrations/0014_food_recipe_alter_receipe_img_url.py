# Generated by Django 4.2.4 on 2023-09-02 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calory_counter', '0013_alter_receipe_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='calory_counter.receipe'),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='img_url',
            field=models.ImageField(blank=True, default='static/recipes/no image.jpeg', null=True, upload_to='static/recipes'),
        ),
    ]

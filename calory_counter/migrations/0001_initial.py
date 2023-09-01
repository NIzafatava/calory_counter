# Generated by Django 4.2.4 on 2023-08-25 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MeatType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meat_name', models.CharField(choices=[('breakfast', 'breakfast'), ('brunch', 'brunch'), ('lunch', 'lunch'), ('dinner', 'dinner'), ('supper', 'supper'), ('snacks', 'snacks')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('calorie', models.FloatField(default=0)),
                ('carbohydrate', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('fats', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('person_of', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

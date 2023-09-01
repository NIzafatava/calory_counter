# Generated by Django 4.2.4 on 2023-08-25 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('calory_counter', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calorie_amount', models.FloatField(blank=True, default=0, null=True)),
                ('amount', models.FloatField(default=0)),
                ('meat_type', models.CharField(max_length=50)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calory_counter.food')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_weight', models.IntegerField(blank=True, default=0)),
                ('goal_weight', models.IntegerField(blank=True, default=0)),
                ('calorie_count', models.FloatField(blank=True, default=0)),
                ('quantity', models.FloatField(default=0)),
                ('total_calorie', models.FloatField(default=0, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('calorie_goal', models.PositiveIntegerField(blank=True, default=1500)),
                ('meat_type', models.CharField(choices=[('breakfast', 'breakfast'), ('brunch', 'brunch'), ('lunch', 'lunch'), ('dinner', 'dinner'), ('supper', 'supper'), ('snacks', 'snacks')], default='breakfast', max_length=50)),
                ('all_food_selected_today', models.ManyToManyField(related_name='inventory', through='user.PostFood', to='calory_counter.food')),
                ('food_selected', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calory_counter.food')),
                ('person_of', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='postfood',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]

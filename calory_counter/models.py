from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import date


# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=200, null=False)
    measure = models.CharField(max_length=200, null=True)
    quantity = models.PositiveIntegerField(null=False, default=0)
    calorie = models.FloatField(null=False, default=0)
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True)
    fats = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True)
    person_of = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    time_hour = models.IntegerField(default=0, blank=True)
    calorie = models.FloatField(null=False, default=0)
    person_of = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Receipe(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=1000000)
    portion = models.PositiveIntegerField(default=1, null=False)
    calorie = models.IntegerField(default=0, blank = True)
    carbohydrate =models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True)
    fats = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True)
    time = models.PositiveIntegerField(default=20, blank=True)
    difficulty_level_options = (
                                ('easy', 'easy'),
                                ('medium', 'medium'),
                                ('difficult', 'difficult'))
    difficulty_level = models.CharField(max_length=50, choices=difficulty_level_options, default='medium')
    ingredients = models.TextField(max_length=1000000, null=True, blank=True)
    img_url = models.ImageField(upload_to='static/recipes', null=True, blank=True, default='static/recipes/no image.jpeg')
    person_of = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
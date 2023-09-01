from django.db import models
from calory_counter.models import *
from django.db.models.signals import post_save
from datetime import date

class Profile(models.Model):
    person_of = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    current_weight = models.IntegerField(default=0, blank=True)
    goal_weight = models.IntegerField(default=0, blank=True)
    calorie_count = models.FloatField(default=0, blank=True)
    food_selected = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    exercises_selected = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, blank=True)
    time_hour_exercise = models.IntegerField(default=0, blank=True)
    calorie_exercise = models.FloatField(null=False, default=0)
    quantity = models.FloatField(default=0)
    total_calorie = models.FloatField(default=0, null=True)
    total_calorie_exercise = models.FloatField(default=0, null=True)
    date = models.DateField(auto_now_add=True)
    calorie_goal = models.PositiveIntegerField(default=1500, blank=True)
    all_food_selected_today = models.ManyToManyField(Food, through='PostFood', related_name='inventory')
    meat_type_choices = (
        ('breakfast', 'breakfast'),
        ('brunch', 'brunch'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('supper', 'supper'),
        ('snacks', 'snacks'),
    )
    meat_type = models.CharField(max_length=50, choices=meat_type_choices, default='breakfast')
    goal_water = models.PositiveIntegerField(null=True, blank=True, default=3)
    current_water = models.FloatField(max_length=100, null=True, blank=True, default=0)


    def save(self, *args, **kwargs):  # new
        if self.food_selected != None:
            self.amount = (self.food_selected.calorie / self.food_selected.quantity)
            self.calorie_count = self.amount * self.quantity
            self.total_calorie = self.calorie_count + self.total_calorie
            calories = Profile.objects.filter(person_of=self.person_of).last()
            PostFood.objects.create(profile=calories, food=self.food_selected, calorie_amount=self.calorie_count,
                                    amount=self.quantity, meat_type=self.meat_type)
            self.food_selected = None
            super(Profile, self).save(*args, **kwargs)
        if self.exercises_selected != None:
            calories = Profile.objects.filter(person_of=self.person_of).last()
            self.amount = (self.exercises_selected.calorie / self.exercises_selected.time_hour)
            self.calorie_count = self.amount * self.time_hour_exercise
            self.total_calorie_exercise = self.calorie_count*self.total_calorie_exercise
            PostExercise.objects.create(profile=calories, exercise=self.exercises_selected, calorie_amount=self.calorie_count,
                                    time=self.time_hour_exercise)
            # PostExercise.objects.create(profile=calories, exercise=self.exercises_selected,
            #                             calorie_amount=self.time_hour_exercise * self.exercises_selected.calorie,
            #                             time=self.time_hour_exercise)
            # PostExercise.objects.create(profile=calories, exercise=self.exercises_selected)
            self.exercises_selected = None
            super(Profile, self).save(*args, **kwargs)
        else:
            super(Profile, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.person_of.username)


def create_profile(sender, instance, created, **kwargs):
    if created:
        person_of_profile = Profile(person_of=instance)
        person_of_profile.save()


post_save.connect(create_profile, sender=User)


class PostFood(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    calorie_amount = models.FloatField(default=0, null=True, blank=True)
    amount = models.FloatField(default=0)
    meat_type = models. CharField(max_length=50)


class PostExercise(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    calorie_amount = models.FloatField(default=0, null=True, blank=True)
    time = models.IntegerField(default=1, blank=True)


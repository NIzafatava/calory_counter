from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import DetailView

from .forms import SelectFoodForm, AddFoodForm, CreateUserForm, ProfileForm, AddExerciseForm, SelectExerciseForm, \
    AddRecipeForm
from .models import *
from datetime import timedelta
from django.utils import timezone
from datetime import date
from datetime import datetime
from .filters import FoodFilter, ExerciseFilter, ReceipeFilter
from user.models import *
from django.http import JsonResponse


@login_required(login_url='user:login')
def HomePageView(request):


    calories = Profile.objects.filter(person_of=request.user).last()
    calorie_goal = calories.calorie_goal
    water_goal = calories.goal_water
    water_current = calories.current_water
    weight = Profile.objects.filter(person_of=request.user).last()
    weight_goal = weight.goal_weight
    date_today = date.today()
    if date.today() > calories.date:
        profile = Profile.objects.create(person_of=request.user)
        profile.save()
    calories = Profile.objects.filter(person_of=request.user).last()
    # calories = Profile.objects.all()
    all_food_today = PostFood.objects.filter(profile=calories)
    all_exercises_today = PostExercise.objects.filter(profile=calories)
    breakfast_all_food_today = PostFood.objects.filter(profile=calories, meat_type__contains='breakfast')
    brunch_all_food_today = PostFood.objects.filter(profile=calories, meat_type__contains='brunch')
    lunch_all_food_today = PostFood.objects.filter(profile=calories, meat_type__contains='lunch')
    dinner_all_food_today = PostFood.objects.filter(profile=calories, meat_type__contains='dinner')
    supper_all_food_today = PostFood.objects.filter(profile=calories, meat_type__contains='supper')
    snacks_all_food_today = PostFood.objects.filter(profile=calories, meat_type__contains='snacks')
    calorie_goal_status = calorie_goal - calories.total_calorie + calories.total_calorie_exercise
    water_goal_status = water_goal - calories.current_water
    weight_goal_status = weight.current_weight - weight_goal
    over_calorie = 0
    if calorie_goal_status < 0:
        over_calorie = abs(calorie_goal_status)
    context = {
        'total_calorie': calories.total_calorie,
        'total_calorie_burned': calories.total_calorie_exercise,
        'calorie_goal': calorie_goal if calorie_goal else 1500,
        'calorie_goal_status': calorie_goal_status,
        'over_calorie': over_calorie,
        'food_selected_today': all_food_today,
        'weight_goal': weight_goal,
        'current_weight': weight.current_weight,
        'weight_goal_status': weight_goal_status,
        'breakfast_all_food_today': breakfast_all_food_today,
        'brunch_all_food_today': brunch_all_food_today,
        'lunch_all_food_today':lunch_all_food_today,
        'dinner_all_food_today':dinner_all_food_today,
        'supper_all_food_today':supper_all_food_today,
        'snacks_all_food_today':snacks_all_food_today,
        'water_goal': water_goal,
        'water_current': water_current,
        'water_goal_status': water_goal_status,
        'all_exercises_today':all_exercises_today,
        'date_today': date_today,
    }
    return render(request, 'home.html', context, )


def receipe_view(request):
    all_receipes = Receipe.objects.all()
    my_filter = ReceipeFilter(request.GET, queryset=all_receipes)
    form = AddRecipeForm(request.POST)
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.person_of = request.user
            profile.save()
            return redirect('calory_counter:receipes')
    else:
        form = AddRecipeForm()
    context = {'all_receipes':all_receipes,
               'my_filter':my_filter,
               'form': form,}
    return render(request, 'receipe_page.html',context,)


class RecipeDetailView(View):
    def get(self, request, recipe_id: int):

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": get_object_or_404(Receipe, id=recipe_id),
            },
        )

@login_required
def select_food(request):
    person = Profile.objects.filter(person_of=request.user).last()
    # food_items = Food.objects.filter(person_of=request.user)
    food_items = Food.objects.all().order_by('name')
    form = SelectFoodForm(request.user, instance=person)
    # form2 = SelectRecipeForm(request.user, instance=person)
    # form2 = SelectRecipeForm(request.user, instance=person)
    myFilter = FoodFilter(request.GET, queryset=food_items)

    if request.method == 'POST':
        form = SelectFoodForm(request.user, request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('calory_counter:home')
    else:
        form = SelectFoodForm(request.user)

    # if request.method == 'POST':
    #     form = SelectRecipeForm(request.user, request.POST, instance=person)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('calory_counter:home')
    # else:
    #     form = SelectRecipeForm(request.user)

    context = {'form': form, 'food_items': food_items, 'my_filter':myFilter}
    return render(request, 'select_food.html', context)

@login_required
def select_exercise(request):
    person = Profile.objects.filter(person_of=request.user).last()
    # food_items = Food.objects.filter(person_of=request.user)
    exercise_items = Exercise.objects.all().order_by('name')
    form = SelectExerciseForm(request.user, instance=person)
    myFilter = ExerciseFilter(request.GET, queryset=exercise_items)

    if request.method == 'POST':
        form = SelectExerciseForm(request.user, request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('calory_counter:home')
    else:
        form = SelectExerciseForm(request.user)

    context = {'form': form, 'exercise_items': exercise_items, 'my_filter':myFilter}
    return render(request, 'select_exercise.html', context)

def add_food(request):

    # food_items = Food.objects.filter(person_of=request.user)
    food_items = Food.objects.all().order_by('name')
    form = AddFoodForm(request.POST)
    if request.method == 'POST':
        form = AddFoodForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.person_of = request.user
            profile.save()
            return redirect('calory_counter:add_food')
    else:
        form = AddFoodForm()

    myFilter = FoodFilter(request.GET, queryset=food_items)
    food_items = myFilter.qs
    context = {'form': form, 'food_items': food_items, 'myFilter': myFilter}
    return render(request, 'add_food.html', context)


def add_exercise(request):

    # food_items = Food.objects.filter(person_of=request.user)
    exercise_items = Exercise.objects.all().order_by('name')
    form = AddExerciseForm(request.POST)
    if request.method == 'POST':
        form = AddExerciseForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.person_of = request.user
            profile.save()
            return redirect('calory_counter:add_exercise')
    else:
        form = AddExerciseForm()

    myFilter = ExerciseFilter(request.GET, queryset=exercise_items)
    exercise_items = myFilter.qs
    context = {'form': form, 'exercise_items': exercise_items, 'myFilter': myFilter}
    return render(request, 'add_exercise.html', context)



@login_required
def update_food(request, pk):
    food_items = Food.objects.filter(person_of=request.user)

    food_item = Food.objects.get(id=pk)
    form = AddFoodForm(instance=food_item)
    if request.method == 'POST':
        form = AddFoodForm(request.POST, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('calory_counter:profile')
    myFilter = FoodFilter(request.GET, queryset=food_items)
    context = {'form': form, 'food_items': food_items, 'myFilter': myFilter}

    return render(request, 'add_food.html', context)



@login_required
def delete_food(request, pk):
    food_item = Food.objects.get(id=pk)
    if request.method == "POST":
        food_item.delete()
        return redirect('calory_counter:profile')
    context = {'food': food_item, }
    return render(request, 'delete_food.html', context)



@login_required
def ProfilePage(request):

    person = Profile.objects.filter(person_of=request.user).last()
    food_items = Food.objects.filter(person_of=request.user)
    form = ProfileForm(instance=person)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('calory_counter:profile')
    else:
        form = ProfileForm(instance=person)


    some_day_last_week = timezone.now().date() - timedelta(days=7)
    records = Profile.objects.filter(date__gte=some_day_last_week, date__lt=timezone.now().date(),
                                     person_of=request.user)

    context = {'form': form, 'food_items': food_items, 'records': records}
    return render(request, 'profile.html', context)


def add_recipe_to_profile(request, recipe_id):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(person_of=request.user).last()
        recipe = Receipe.objects.get(pk=recipe_id)
        profile.recipes.add(recipe)
        # profile.update_total_calorie()

        return redirect('calory_counter:add_food')
    else:

        return redirect('user:login')


def get_statistic_view(request):
    return render(request, 'statistics.html')

def get_statistics_calorie(request):
    labels = []
    data = []

    queryset = Profile.objects.values('date', 'total_calorie')
    for entry in queryset:
        labels.append(entry['date'])
        data.append(entry['total_calorie'])

    # return render(request, 'statistics.html')
    return JsonResponse(data={
            'labels': labels,
            'data': data,
        })


def get_statistics_weight(request):
    labels = []
    data = []

    queryset = Profile.objects.values('date', 'current_weight')
    for entry in queryset:
        labels.append(entry['date'])
        data.append(entry['current_weight'])

    # return render(request, 'statistics.html')
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def get_statistics_water(request):
    labels = []
    data = []

    queryset = Profile.objects.values('date', 'current_water')
    for entry in queryset:
        labels.append(entry['date'])
        data.append(entry['current_water'])

    # return render(request, 'statistics.html')
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
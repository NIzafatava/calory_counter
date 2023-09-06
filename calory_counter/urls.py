from django.urls import path

from .views import (HomePageView, select_food, add_food, ProfilePage, update_food, delete_food, add_exercise, \
	select_exercise, receipe_view, RecipeDetailView, add_recipe_to_profile, get_statistics_calorie,
					get_statistic_view, get_statistics_weight)



app_name = 'calory_counter'

urlpatterns = [
	path('', HomePageView,name='home'),
	path('select_food/',select_food,name='select_food'),
	path('select_exercise/', select_exercise, name='select_exercise'),
	path('add_food/',add_food,name='add_food'),
	path('add_exercise/',add_exercise,name='add_exercise'),
	path('update_food/<str:pk>/',update_food,name='update_food'),
	path('delete_food/<str:pk>/',delete_food,name='delete_food'),
	path('profile/',ProfilePage,name='profile'),
	path('receipes/',receipe_view,name='receipes'),
	path('receipes/<int:recipe_id>/', RecipeDetailView.as_view(), name='show'),
	path('add_recipe/<int:recipe_id>/', add_recipe_to_profile, name='add_recipe'),
	path('statistics/', get_statistics_calorie, name ='statistics_calorie'),
	path('statistics_weight/', get_statistics_weight, name='statistics_weight'),
	path('statistics_view/', get_statistic_view, name='statistics_view'),
]
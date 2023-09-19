import django_filters
from admin_searchable_dropdown.filters import AutocompleteFilter
from django.contrib import admin
from django_filters import CharFilter

from .models import *


class FoodFilter(django_filters.FilterSet):
    food_name = CharFilter(
        field_name="name", lookup_expr="icontains", label="Search existing food:"
    )

    class Meta:
        model = Food
        fields = ["food_name"]


class ReceipeFilter(django_filters.FilterSet):
    receipe_item = CharFilter(
        field_name="content", lookup_expr="icontains", label="Search receipe:"
    )

    class Meta:
        model = Receipe
        fields = ["receipe_item"]


class ExerciseFilter(django_filters.FilterSet):
    exercise_name = CharFilter(
        field_name="name", lookup_expr="icontains", label="Search existing exercise"
    )

    class Meta:
        model = Exercise
        fields = ["exercise_name"]


class FoodSelectFilter(AutocompleteFilter):
    title = "Food select"
    field_name = "food_selected"


class FoodAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class ProfileAdmin(admin.ModelAdmin):
    list_filter = [FoodSelectFilter]

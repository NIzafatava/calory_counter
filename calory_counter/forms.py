from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Food, Exercise, Receipe
from user.models import Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SelectFoodForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('food_selected', 'quantity','meat_type',)

    def __init__(self, user, *args, **kwargs):
        super(SelectFoodForm, self).__init__(*args, **kwargs)
        # self.fields['food_selected'].queryset = Food.objects.filter(person_of=user)
        self.fields['food_selected'].queryset = Food.objects.all().order_by('name')


class SelectExerciseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('exercises_selected', 'time_hour_exercise',)

    def __init__(self, user, *args, **kwargs):
        super(SelectExerciseForm, self).__init__(*args, **kwargs)
        # self.fields['food_selected'].queryset = Food.objects.filter(person_of=user)
        self.fields['exercises_selected'].queryset = Exercise.objects.all().order_by('name')


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Receipe
        fields = ('name', 'content', 'ingredients', )
        widgets = {
            'ingredients': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'ingredients'
            }),
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'recipe name'
            }),
            'content': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'content'
            })

        }


class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name', 'measure', 'calorie', 'carbohydrate', 'fats', 'protein',)


class AddExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('name', 'time_hour', 'calorie',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('calorie_goal', 'goal_weight', 'current_weight', 'goal_water','current_water',)





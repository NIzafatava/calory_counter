from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import ChoiceWidget

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
        labels = {'food_selected': 'Food',
        'quantity':'Qnty', 'meat_type': 'Type'}


    def __init__(self, user, *args, **kwargs):
        super(SelectFoodForm, self).__init__(*args, **kwargs)
        # self.fields['food_selected'].queryset = Food.objects.filter(person_of=user)
        self.fields['food_selected'].queryset = Food.objects.all().order_by('name')
        self.fields['food_selected'].widget.attrs['style'] = 'width:200px; height:20px;border-color: black;'
        self.fields['quantity'].widget.attrs['style'] = 'width:200px; height:20px; background: white;border-color: black;'
        self.fields['meat_type'].widget.attrs['style'] = 'width:200px; height:20px;border-color: black;'

# class SelectRecipeForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('recipe_selected', 'quantity','meat_type',)
#
#     def __init__(self, user, *args, **kwargs):
#         super(SelectRecipeForm, self).__init__(*args, **kwargs)
#         # self.fields['food_selected'].queryset = Food.objects.filter(person_of=user)
#         self.fields['recipe_selected'].queryset = Receipe.objects.all().order_by('name')

class SelectExerciseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('exercises_selected', 'time_hour_exercise',)


    def __init__(self, user, *args, **kwargs):
        super(SelectExerciseForm, self).__init__(*args, **kwargs)
        # self.fields['food_selected'].queryset = Food.objects.filter(person_of=user)
        self.fields['exercises_selected'].queryset = Exercise.objects.all().order_by('name')
        self.fields['exercises_selected'].widget.attrs['style'] = 'width:200px; height:20px; background: white;border-color: black;'
        self.fields['time_hour_exercise'].widget.attrs['style'] = 'width:200px; height:20px;border-color: black;'


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
        fields = ('name', 'measure', 'calorie', 'quantity', 'carbohydrate', 'fats', 'protein',)

        def __init__(self, user, *args, **kwargs):
            super(AddFoodForm, self).__init__(*args, **kwargs)



class AddExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('name', 'time_hour', 'calorie',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('calorie_goal', 'goal_weight', 'current_weight', 'goal_water','current_water',)





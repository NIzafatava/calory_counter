from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from calory_counter.forms import CreateUserForm
from .models import *
from datetime import timedelta
from django.utils import timezone
from datetime import date
from datetime import datetime
from user.models import *


# Create your views here.
def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('calory_counter:home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)
                return redirect('user:login')

        context = {'form': form}
        return render(request, 'register.html', context)



def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('calory_counter:home')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('calory_counter:home')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'login.html', context)



def LogOutPage(request):
    logout(request)
    return redirect('user:login')


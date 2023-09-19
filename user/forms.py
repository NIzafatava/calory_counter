from django import forms
from django.contrib.auth.forms import UserCreationForm

# from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError

from .models import User


class EmailForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError("Пользователя с таким email не существует!")
        return email


class ResetPasswordForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["password1"]

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views import View

from calory_counter.forms import CreateUserForm
from .email import ResetPasswordEmailSender
from .forms import EmailForm, ResetPasswordForm
from .tasks import send_register_email


class Register(View):
    def get(self, request):
        return render(request, "register.html", {"form": CreateUserForm()})

    def post(self, request):
        form = CreateUserForm(request.POST)

        if not form.is_valid():
            return render(request, "register.html", {"form": form})

        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = str(get_current_site(request))

        send_register_email.delay(current_site, user.id)

        return redirect(reverse("user:login"))


class ConfirmRegisterView(View):
    def get(self, request, uidb64: str, token: str):
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(get_user_model(), id=uid)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse("<h1>Спасибо, что подтвердили регистрацию!</h1>")

        return HttpResponse("<h1>Ссылка неверная</h1>")


class ResetPasswordView(View):
    def get(self, request):
        return render(request, "reset_password.html", {"form": EmailForm()})

    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(get_user_model(), email=form.cleaned_data["email"])
            email_sender = ResetPasswordEmailSender(request, user)
            email_sender.send_email()
            return HttpResponse("<h1>Проверьте почту, для сброса пароля!</h1>")

        return render(request, "reset_password.html", {"form": form})


class ConfirmResetPasswordView(View):
    def get(self, request, uidb64: str, token: str):
        return render(
            request,
            "confirm_reset_password.html",
            {"form": ResetPasswordForm()},
        )

    def post(self, request, uidb64: str, token: str):
        # Пример URL /Mjg/bqgzrh-6147c5ab396a08a5541ceb05e6c11e01

        uid = force_str(
            urlsafe_base64_decode(uidb64)
        )  # Получаем идентификатор пользователя из `Mjg`
        user = get_object_or_404(get_user_model(), id=uid)

        form = ResetPasswordForm(request.POST)
        # Проверяем форму и токен - `bqgzrh-6147c5ab396a08a5541ceb05e6c11e01`
        if form.is_valid() and default_token_generator.check_token(user, token):
            user.set_password(form.cleaned_data["password1"])
            user.save()
            return redirect(reverse("accounts:login"))

        return render(request, "reset_password.html", {"form": form})


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect("calory_counter:home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("calory_counter:home")
            else:
                messages.info(request, "Username or password is incorrect")
        context = {}
        return render(request, "login.html", context)


def LogOutPage(request):
    logout(request)
    return redirect("user:login")

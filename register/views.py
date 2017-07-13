from .forms import RegisterForm, LoginForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, FormView, RedirectView


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = "register/register.html"
    form_class = RegisterForm
    success_url = "/"
    success_message = "Регистрация прошла успешно"

    def form_valid(self, form):
        user = form.save()
        user.save()
        username = user.username
        password = user.password
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


class SignUp(SuccessMessageMixin, FormView):
    template_name = "register/register.html"
    form_class = RegisterForm
    success_url = "/"
    success_message = "Регистрация прошла успешно"


class SignIn(FormView):
    template_name = "register/login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(SignIn, self).form_valid(form)


class Logout(RedirectView):
    url = "/"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)

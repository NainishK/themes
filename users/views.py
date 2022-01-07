from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class RegisterView(TemplateView):
    template_name = 'users/company-signup.html'


class LoginView(TemplateView):
    template_name = 'users/company-login.html'

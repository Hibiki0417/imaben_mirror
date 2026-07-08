from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.
class ManagerLogin(LoginView):
    template_name = "manager/manager_login.html"
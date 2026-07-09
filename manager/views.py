from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ManagerLogin(LoginView):
    template_name = "manager/manager_login.html"

class ManagerDashboard(LoginRequiredMixin, TemplateView):
    template_name = "manager/dashboard.html"
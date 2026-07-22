from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from shops.models import Shop
# Create your views here.
class ManagerLogin(LoginView):
    template_name = "manager/manager_login.html"

class ManagerDashboard(LoginRequiredMixin, TemplateView):
    template_name = "manager/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shop"] = Shop.objects.first()
        return context
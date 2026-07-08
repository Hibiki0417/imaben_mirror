from django.urls import path
from . import views

app_name = "manager"

urlpatterns = [
    path("login/", views.ManagerLogin.as_view(), name="manager_login"),
    
]
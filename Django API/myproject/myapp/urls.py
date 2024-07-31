
from django.urls import path
from .views import RegisterView, LoginView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
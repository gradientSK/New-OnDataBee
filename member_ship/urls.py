from django.urls import path
from . import views

urlpatterns = [
    path('user_login', views.user_login),
    path('signup/', views.register_user),
]
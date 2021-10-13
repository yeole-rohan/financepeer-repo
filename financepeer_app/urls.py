from os import name
from django.urls import path
from django.contrib.auth import views
from . import views as app_views
urlpatterns = [
    path("accounts/login/", views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path("accounts/logout/", views.LogoutView.as_view(), name="logout"),
    path('accounts/signup/', app_views.signup, name="signup"),
    path('', app_views.home, name="home"),
    
]

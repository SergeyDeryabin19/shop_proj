from django.urls import path
from django.contrib.auth import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignUpView
from . import views


app_name = 'staff'
urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name='login.html'),
    path("logout/", views.LogoutView.as_view(), name='logout.html'),
    path('signup/', views.SignUpView.as_view(), name='singup.html'),
]
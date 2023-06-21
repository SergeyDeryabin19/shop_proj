from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from directories import views


# Create your views here.

class CustomLoginView(LoginView):
   template_name = 'auntification/login.html'
   form_class = AuthenticationForm
   

class CustomLogoutView(LogoutView):
   template_name = 'auntification/logout.html'
   next_page = 'book_parametrs/home_page.html'

class SignUpView(CreateView):
    model = User
    template_name = 'auntification/signup.html'
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('book_parametrs/home_page.html')
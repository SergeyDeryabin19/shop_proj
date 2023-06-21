from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from directories import views
from django.shortcuts import redirect


# Create your views here.

class CustomLoginView(LoginView):
   template_name = 'auntification/login.html'
   # form_class = AuthenticationForm
   # success_url = reverse_lazy('homepage:success.html')
   
   # def form_valid(self, form):
   #    response = super().form_valid(form)
   #    next_url = self.request.GET.get('next', reverse_lazy('home'))
   #    if self.request.user.is_authenticated:
   #       next_url += f'?logged_in=True'
   #       return redirect(next_url)

   


class CustomLogoutView(LogoutView):
   template_name = 'auntification/logout.html'
   # success_url = reverse_lazy('success.html')
   # next_page = 'success.html'

class SignUpView(CreateView):
    model = User
    template_name = 'auntification/signup.html'
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('success.html')
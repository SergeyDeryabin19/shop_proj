"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from directories import views
from directories import urls




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view()),
    path('directories/', include('directories.urls'), name='directories'),
    path('staff/', include('staff.urls'), name='staff'),
    path('success', views.success_page, name='success.html'),
    path('oh_no_problem', views.Oh_no_problem.as_view(), name='oh_no_problem.html'),
  
]


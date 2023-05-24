from django.shortcuts import render
from . import models

# Create your views here.

def genres_vew(request):
    genres = models.Genres.objects.all()  
    return render(
        request, 
        template_name = "book_parametrs/genres.html", 
        context={'objects': genres}
        )
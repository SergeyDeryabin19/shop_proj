from django.shortcuts import render, redirect
from . import models
from .forms import AddGenreForm

# Create your views here.

def genres_vew(request):
    genres = models.Genres.objects.all()  
    return render(
        request, 
        template_name = "book_parametrs/genres.html", 
        context={'objects': genres}
        )


def author_vew(request):
    authors = models.Author.objects.all()  
    return render(
        request, 
        template_name = "book_parametrs/author.html", 
        context={'objects': authors}
        )


def series_vew(request):
    series = models.Series.objects.all()  
    return render(
        request, 
        template_name = "book_parametrs/series.html", 
        context={'objects': series}
        )


def publishing_vew(request):
    publishing = models.Publishing.objects.all()  
    return render(
        request, 
        template_name = "book_parametrs/publishing.html", 
        context={'objects': publishing}
        )
    
def add_genre(request):
    genre_name = request.POST.get("genre name")
    genre_description = request.POST.get("genre description")
    print(genre_name)
    print(genre_description)
    new_genre = models.Genres.objects.create(name=genre_name, description=genre_description)
    return render(
        request, 
        template_name = "book_parametrs/add_genre.html", 
        context={}
    )

def add_genre_forms(request):
    if request.method == "POST":
        form = AddGenreForm(request.POST)
        if form.is_valid():
            # сохранение объекта модели
            return redirect("genres.html")
    else:
        form = AddGenreForm()
    return render(request, "book_parametrs/add_genre_forms.html", {"form": form})


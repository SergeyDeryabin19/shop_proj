from django import forms
from django.shortcuts import render, redirect
from .models import Genres
from . import models

class AddGenreForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)

def add_genre_forms(request):
    if request.method == "POST":
        form = AddGenreForm(request.POST)
        if form.is_valid():
            name_new = form.cleaned_data["name"]
            description_new = form.cleaned_data["description"]
            new_genre = models.Genres.objects.create(name=name_new, description=description_new)
            return redirect("genre_list")
    else:
        form = AddGenreForm()
    return render(request, "book_parametrs/add_genre_forms.html", {"form": form})
from django.shortcuts import render
from . import models
from django.views import generic

# Create your views here.

class BookListView(generic.ListView):
    model = models.Book
    template_name = "book/book_view_all.html"

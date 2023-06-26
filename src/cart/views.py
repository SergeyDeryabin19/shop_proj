from django.shortcuts import render
from django.views import generic

# Create your views here.

# Работа с моделью книги в корзине, процесс добавления книги в корзину, если 
# книги нет, ее добавляет в корзину, если книга есть, увеличивает количество в 
# корзине на 1 штуку
class AddBookToCart(generic.View):
    None



# Работа с моделью корзина, включает видимы методы
class CartView(generic.DetailView):
    None
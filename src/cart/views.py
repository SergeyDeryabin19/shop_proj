from django.db import models
from django.shortcuts import render
from django.views import generic
from .models import Cart, Book, BookInCart
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import View
from . import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Работа с моделью книги в корзине, процесс добавления книги в корзину, если 
# книги нет, ее добавляет в корзину, если книга есть, увеличивает количество в 
# корзине на 1 штуку
# Работа с моделью корзина, включает видимые методы

class CartView(generic.TemplateView):
    model = models.Cart
    template_name = "cart/cart_view.html"

    def get_context_data(self, **kwargs):
        pk = self.request.session.get("cart_id")
        context = super().get_context_data(**kwargs)
        # Получаем текущего пользователя
        user = self.request.user
        # Если пользователь анонимный, то устанавливаем его значение в None
        if user.is_anonymous:
            user = None
            cart, created = models.Cart.objects.get_or_create(pk=pk)
        # Получаем или создаем корзину пользователя
        else: cart, created = models.Cart.objects.get_or_create(user=user)
        # cart, created = models.Cart.objects.get_or_create(pk=pk)
        print(cart, 'asfasf')
        # Получаем все товары, находящиеся в корзине
        books_in_cart = cart.books.all()
        context["cart"] = cart
        context["books_in_cart"] = books_in_cart
        return context
    
    
    
class CartUpdateView(generic.DetailView):
    model = models.Cart
    def update_cart(request):
        if request.method == 'POST':
            book_id = request.POST.get('book_id')
            print(request.POST.get('book_id'))
            count = int(request.POST.get('count'))
            print(int(request.POST.get('count')))
            book = Cart.objects.get(book_id=book_id)
            book.count = count
            book.save()

        return redirect('cart')
    
        
        

    
    # @property
    # def total_price(self):
    #     total_price = 0
    #     for item_in_cart in self.items.all():
    #         total_price += item_in_cart.price
    #     return total_price

    
class AddBookToCart(generic.DetailView):
    def get(self, request, *args, **kwargs):
        pk = self.request.session.get("cart_id")
        print(self.request.session.get("cart_id"))
        user = self.request.user
        print(user)
        if user.is_anonymous:
            user=None
            print("заходит в цикл анонимус")
            print(pk, type(pk))
        # if user is None:
            # cart = models.Cart.objects.create(user=user)
            cart, created = models.Cart.objects.get_or_create(pk=pk)
            print("заходит в циклпк из нон")
            self.request.session['cart_id'] = cart.pk  
            print(self.request.session['cart_id'])
        elif request.user.is_authenticated:
            print("here is auntificated")
            cart, created = models.Cart.objects.get_or_create(user=user)
        book_pk = kwargs.get("pk")
        book = models.Book.objects.get(pk=book_pk)
        if cart.check_if_book_already_in_cart(book):
            book_in_cart = BookInCart.objects.get(cart=cart, book=book)
            book_in_cart.count += 1
            book_in_cart.save()
            return redirect(to=reverse("book:book_detail.html", kwargs={
                "pk": book_pk
            }))
        else:
            book_in_cart = BookInCart.objects.create(
            book=book,
            count=1,
        )
            cart.books.add(book_in_cart)
        return redirect(to=reverse("book:book_detail.html", kwargs={  
            "pk": book_pk
        }))


class OrderView(generic.ListView):
    model = models.Order
    template_name = "cart/order_view.html"



# class AddBookToCart(generic.View):
#     def get(self, request, *args, **kwargs):
#         user = request.user
#         cart = Cart.objects.get(user=user)
#         book_pk = kwargs.get("pk")
#         book = Book.objects.get(pk=book_pk)
#         if cart.check_if_book_already_in_cart(book):
#             return redirect(to=reverse("book:book_detail.html", kwargs={
#                 "pk": book_pk
#             }))
#         book_in_cart = BookInCart.objects.create(
#             book=book,
#             count=1,
#         )
#         cart.books.add(book_in_cart)
#         return redirect(to=reverse("book:book_detail.html", kwargs={  
#             "pk": book_pk
#         }))
    
        # Добавьте другие данные, которые вам нужно передать в шаблон
# class CartView(generic.DetailView):
#     model = Cart
#     template_name = "cart/cart_view.html"
    
#     def get_object(self, request):
#         cart_id = self.request.GET.get('cart_id')
#         return cart_id
   
    # def get_object(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Cart.objects.get(user=user, id=self.kwargs.get('cart_id'))
    #     return None

    # def post(self, request, *args, **kwargs):
    #     cart = self.get_object()

    #     if "checkout" in request.POST:
    #         order = Order.objects.create(user=cart.user, total_price=cart.get_total_price())
    #         for book_in_cart in cart.books.all():
    #             order.books.add(book_in_cart)
    #         cart.clear_cart()

    #         return redirect('cart:view_cart', cart_id=cart.id)
    #     else:
    #         item_id = request.POST.get("item_id")
    #         count = request.POST.get("count")
    #         cart.update_count(item_id, count)
    #         return redirect('cart:view_cart', cart_id=cart.id)

    # def remove_item(request, cart_id, item_id):
    #     cart = Cart.objects.get(id=cart_id)
    #     item = cart.books.get(id=item_id)
    #     item.delete()
    #     return redirect('cart:view_cart', cart_id=cart.id)


    # def order_details(request, order_id):
    #     order = Order.objects.get(id=order_id)
    #     return render(request, 'cart/order_details.html', {'order':order})

    # def clear_cart(self):
    #     self.books.clear()
from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    # path('view_book', views.BookListView.as_view(), name='book_view_all.html'),
    # path('book_add', views.BookCreateView.as_view(), name='book_add.html'),
    # path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail.html'),
    # path('book_update/<int:pk>', views.BookUpdateView.as_view(), name='book_update.html'),
    # path('book_delete/<int:pk>', views.BookDeleteView.as_view(), name='book_delete.html')
    path('book_add_to_cart/<int:pk>', views.AddBookToCart.as_view(), name='book_add_to_cart.html'),
    path('cart_view', views.CartView.as_view(), name='cart_view'),
    path('cart/<int:cart_id>/<int:item_id>/', views.CartUpdateView.update_cart, name='update_cart'),
    # path('cart/<int:cart_id>/remove/<int:item_id>/', views.CartView.remove_item, name='remove_item')
    path('order/', views.OrderView.as_view(), name='order'),
    ]
    
    
    

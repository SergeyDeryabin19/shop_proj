from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.BookListView.as_view(), name='book_view_all.html')
    
    
    
    

]
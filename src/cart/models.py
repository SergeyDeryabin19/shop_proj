from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from book.models import Book

# Create your models here.

#Модель(первая часть корзины), из нее берем книги(из книг вытягивать имя, цену), количество
class BookInCart(models.Model):
    # Через переменную book связываемся с моделью Book для вытягивания нужных нам данных
    book = models.ForeignKey(
        to=Book, 
        on_delete=models.CASCADE
    )
    # Водим переменную count, которая представляет собой количество книг в корзине(для дальнейшего подсчета общей стоимости корзины)
    count = models.PositiveIntegerField(
        default=1
    ) 
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     Cart.total_count = self.cart.get_total_count_of_cart()
    #     self.cart.total_price = self.cart.get_cart_price()
    #     self.cart.save()
    
#Модель(вторая ччасть корзины), в ней определенный пользователь которому присвоена определенная корзина
class Cart(models.Model):
    user = models.OneToOneField(
        to=User, 
        on_delete=models.PROTECT, 
        null=True,
        blank=True
        )
    # переменная books вытягивает из модели BookInCart все добавленые книги(книги добавленные в корзину), 
    # для дальнейшего подсчета стоимости корзины
    books = models.ManyToManyField(
        to=BookInCart,
        verbose_name="Books in cart",
        blank=True
    )
    created = models.DateTimeField(
        verbose_name="Created",
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name="Updated",
        auto_now_add=False,
        auto_now=True
    )
    
    
    #  Сумарное количество книг в корзине
    @property
    def get_result_price_of_cart(self):
        total_price=0
        for book_in_cart in self.books.all():
            price = book_in_cart.book.price
            count = book_in_cart.count
            total_price+= price*count
        return total_price
    
    # Подсчет стоимости товарной позиции при изменении количества
    def update_count(self, item_id, count):
        book_in_cart = self.books.get(id=item_id)
        book_in_cart.count = count
        book_in_cart.save()
    
    # Сумарное количество книг в корзине
    # @property
    # def get_total_count_of_cart(self):
    #     total_cart_count = 0
    #     for book_in_cart in self.books.all():
    #         count = book_in_cart.count
    #         total_cart_count += count
    #     return total_cart_count
    
    
    
    # Стоимость одной книги
    # def get_cart_price(self):
    #     total_cart_price = 0
    #     for book_in_cart in self.books.all():
    #         book = book_in_cart.book
    #         count = book_in_cart.count
    #         total_cart_price += book.price * count
    #     return total_cart_price
    
    # Очищает корзину при оформлении заказа
    def clear_cart(self):
        self.books.clear()
        return ...
    
    # Проверка на наличие книги в корзине, если нет, добавляем, если есть, +1
    def check_if_book_already_in_cart(self, book_to_check):
        for book_in_cart in self.books.all():
            checked_book= book_in_cart.book
            if checked_book == book_to_check:
                return True
           
    
    
    # Если для выполнения процесса нужно физическое воздействие для выполнения
    # этого процесса, то пишем во вьюхе, если процесс выполняется гдето там, 
    # а мы видим только результат выполнения процесса, то метод пишем в модели
    
    
# По сути мы создали все необходимы модели для осущесвления процесса заказа книг через корзину, у нас есть все данные,
# а именно, из модели BookInCart столбцы book(содержит все данные о добавленных книгах) count(количество конкретных книг которые 
# пользователь хочет заказать), из модели Cart один пользователь user который формирует корзину, и все книги books которые он заказал


# Модель заказ, нужные нам поля кто заказал, куда заказал, что заказали(корзина в которой что заказали сколько, сумарная стоимость),
# когда заказали, статус заказа когда был создан заказ
class Order(models.Model):
    user = models.ForeignKey(
        to=User,
        verbose_name="Customer",
        on_delete=models.CASCADE,
        blank=False
        )
    delivery_adress = models.TextField(
        verbose_name="Delivery adress"
        )
    cart = models.OneToOneField(
        to=Cart, 
        verbose_name="Cart",
        on_delete=models.CASCADE
        )
           
    price = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        default=0
        )

    STATUS = (
        ('In process', 'In process'),
        ('Something wrong', 'Something wrong'),
        ('Ready', 'Ready'),
    )
    status = models.CharField(
        max_length=255,
        choices = STATUS,
        verbose_name="Order status"
    )
    created = models.DateTimeField(
        verbose_name="Created",
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name="Updated",
        auto_now_add=False,
        auto_now=True
    )

    def str(self):
        return f"Order {self.id} by {self.user.username} on {self.created_at}"
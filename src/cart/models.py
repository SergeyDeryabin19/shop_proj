from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from book.models import Book


#Модель(первая часть корзины), из нее берем книги(из книг вытягивать имя, цену), количество
class BookInCart(models.Model):
    # Через переменную book связываемся с моделью Book для вытягивания нужных нам данных
    book = models.ForeignKey(
        to=Book, 
        on_delete=models.PROTECT
        )
    # Водим переменную count, которая представляет собой количество книг в корзине(для дальнейшего подсчета общей стоимости корзины)
    count = models.PositiveIntegerField(
        default=1
)
    
#Модель(вторая ччасть корзины), в ней определенный пользователь которому присвоена определенная корзина
class Cart(models.Model):
    user = models.OneToOneField(
        to=User, 
        on_delete=models.PROTECT, 
        unique=True
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
# По сути мы создали все необходимы модели для осущесвления процесса заказа книг через корзину, у нас есть все данные,
# а именно, из модели BookInCart столбцы book(содержит все данные о добавленных книгах) count(количество конкретных книг которые 
# пользователь хочет заказать), из модели Cart один пользователь user который формирует корзину, и все книги books которые он заказал


# Модель заказ, нужные нам поля кто заказал, куда заказал, что заказали(корзина в которой что заказали сколько, сумарная стоимость),
# когда заказали, статус заказа когда был создан заказ
class Order(models.Model):
    user = models.ForeignKey(
        to=User,
        verbose_name="Customer",
        on_delete=models.PROTECT
        )
    delivery_adress = models.TextField(
        verbose_name="Delivery adress"
        )
    cart = models.OneToOneField(
        to=Cart, 
        verbose_name="Cart",
        on_delete=models.PROTECT
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
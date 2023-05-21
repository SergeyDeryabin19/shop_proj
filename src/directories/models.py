from django.db import models

# Create your models here.

class Genres(models.Model): #жанры
    name = models.CharField(
        verbose_name="Genre name",  #название жанра
        max_length=20
        )
    description = models.TextField(
        verbose_name="Genre description",   #значение жанра
        null=True,
        blank=True        
    )
    # def __str__(self):
    #     return self.name
from django.db import models

# Create your models here.

class Genres(models.Model): 
    def __str__(self):
        return self.name
    
    name = models.CharField(
        verbose_name="Genre name",  
        max_length=255
        )
    
    description = models.TextField(
        verbose_name="Genre description",   
        null=True,
        blank=True        
    )

class Author(models.Model): 
    def __str__(self):
        return self.name
    
    name = models.CharField(
        verbose_name="Author name",  
        max_length=255
        )
    
    description = models.TextField(
        verbose_name="Basic information",   
        null=True,
        blank=True        
    )    

class Series(models.Model): 
    def __str__(self):
        return self.name
    
    name = models.CharField(
        verbose_name="Series count",  
        max_length=255
        )
    
    description = models.TextField(
        verbose_name="Series information",   
        null=True,
        blank=True        
    )    
    
class Publishing(models.Model): 
    def __str__(self):
        return self.name
    
    name = models.CharField(
        verbose_name="Publishing name",  
        max_length=255
        )
    
    description = models.TextField(
        verbose_name="Publishing information",   
        null=True,
        blank=True        
    )    
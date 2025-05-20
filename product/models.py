from django.db import models

# Create your models here.
class Category(models.TextChoices):
    COMPUTERS='computer'
    FOOD='food'
    KIDS='Kids'

class Product(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField(max_length=500)
    price=models.DecimalField(max_digits=7,decimal_places=3,default=0.0)
    category=models.CharField(max_length=30,choices=Category.choices)
    stock=models.PositiveIntegerField()
    image=models.ImageField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} of category {self.category}'





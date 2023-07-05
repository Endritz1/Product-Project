from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        ordering = ("name",)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

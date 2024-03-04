from django.db import models
from datetime import datetime
class UserDetails(models.Model):
    Name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=10)

class ProductCategory(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.name
        
class Products(models.Model):
    name = models.CharField(max_length=30)
    ProductDescription = models.TextField(max_length=254)
    category= models.ForeignKey(ProductCategory,on_delete=models.CASCADE,default=1 )    
    Brand = models.CharField(max_length=254)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    productimage = models.ImageField(upload_to='images') 
    Created_at =  models.DateTimeField(default=datetime.now,blank=True)
class Cart(models.Model):
    user = models.ForeignKey(UserDetails, null=True, blank=True, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: {} has {} items in their cart. Their total is ${}".format(self.user, self.count, self.total)


class Entry(models.Model):
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "This entry contains {} {}(s).".format(self.quantity, self.product.name)

# Create your models here.

from cgi import print_exception
from distutils.command.upload import upload
from multiprocessing.dummy import active_children
from tabnanny import verbose
from tkinter import CASCADE
from tkinter.tix import Tree
from unicodedata import category
from django.db import models
from matplotlib.style import available
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to="category",blank=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    
    def get_url(self):
        return reverse('products_by_category',args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=250,unique=False)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to="product",blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name='product'
        verbose_name_plural='products'
    
    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])


    def __str__(self):
        return self.name

class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=['date_added']
    
    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product
    
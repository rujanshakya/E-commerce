from cgi import print_exception
from distutils.command.upload import upload
from tabnanny import verbose
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
    slug=models.SlugField(max_length=250,unique=False)
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

    def __str__(self):
        return self.name
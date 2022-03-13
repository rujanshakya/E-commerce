from unicodedata import category
from django.shortcuts import get_object_or_404, render
from matplotlib.style import available
from .models import Category,Product
# Create your views here.
def home(request,category_slug=None):
    category_page=None
    products=None
    if category_slug!=None:
        category_page=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=category_page,available=True)
    else:
        products=Product.objects.all().filter(available=True)
    return render(request,"home.html",{'category':category_page,'products':products})

def productPage(request,category_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,"product.html",{'product':product})
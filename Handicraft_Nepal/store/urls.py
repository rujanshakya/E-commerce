from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('category/<slug:category_slug>',views.home,name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>',views.productPage,name='product_detail'),
]
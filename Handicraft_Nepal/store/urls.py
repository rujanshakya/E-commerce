from unicodedata import name
from django.urls import path
from .import views
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('category/<slug:category_slug>',views.home,name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>',views.productPage,name='product_detail'),
    path('cart/add/<int:product_id>',views.add_cart,name="add_cart"),
    path('cart/',views.cart_detail,name='cart_detail'),
    path('cart/remove/<int:product_id>',views.cart_remove,name="cart_remove"),
    path('cart/remove_product/<int:product_id>',views.cart_remove_product,name="cart_remove_product"),
    path('thankyou/',views.thanks_page,name='thanks_page')
]
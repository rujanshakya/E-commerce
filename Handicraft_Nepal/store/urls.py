from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:category_slug>',views.home,name='products_by_category'),
    path('product/',views.productPage,name='product'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
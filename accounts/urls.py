from django.urls import path
from . import views
from django.contrib import admin  
from django.urls import path  
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  
urlpatterns = [
    path('', views.home, name = 'home'),
    path('Form/',views.Form,name='Form'),
    path('sign/', views.sign, name='sign'),  
    path('products/', views.products, name='products'),
    path('Cloth/<int:category_id>', views.Cloth, name='Cloth'),
    path('detail/<int:pk>', views.detail,name='detail'),
    path('addToCart/', views.addToCart, name='addToCart'),

]


if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
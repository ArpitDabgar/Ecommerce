"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('', views.index, name='index'),
    path('filter_price', views.filter_price, name='filter_price'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('add_wishlist/<int:id>/', views.add_wishlist, name='add_wishlist'),
    path('delete_wishlist/<int:id>/', views.delete_wishlist, name='delete_wishlist'),
    path('cart', views.cart, name='cart'),
    path('add_cart/<int:id>/', views.add_cart, name='add_cart'),
    path('cart_increment/<int:id>/', views.cart_increment, name='cart_increment'),
    path('cart_decrement/<int:id>/', views.cart_decrement, name='cart_decrement'),
    path('cart_delete/<int:id>/', views.cart_delete, name='cart_delete'),
    path('apply_coupon', views.apply_coupon, name='apply_coupon'),
    path('checkout', views.checkout, name='checkout'),
    path('billing_view', views.billing_view, name='billing_view'),
    path('contact', views.contact, name='contact'),
    path('error', views.error, name='error'),
    path('shop_detail', views.shop_detail, name='shop_detail'),
    path('shop_detail1/<int:id>/', views.shop_detail1, name='shop_detail1'),
    path('shop', views.shop, name='shop'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('login', views.login, name='login'),  
    path('logout', views.logout, name='logout'), 
    path('register', views.register, name='register'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('confirm_password', views.confirm_password, name='confirm_password'),
    
]
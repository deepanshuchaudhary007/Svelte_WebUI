"""
URL configuration for Svelte_Web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Svelte_Web import views

urlpatterns = [
    path('admin/', admin.site.urls),          
    # path('country/', views.country, name='country'),
    path('state/<int:id>', views.state, name='country'),
    path('city/<int:id>', views.city, name='country'),

    path('blog_single/', views.blog_single, name='blog_single'), 
    path('blog/', views.blog, name='blog'),    
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact_us/', views.contact_us, name='contact_us'),    
    path('', views.index, name='index'),    
    path('product_details/<str:slug>', views.product_details, name='product_details'),
    path('category_filter/<str:slug>', views.category_filter, name='category_filter'), 
    path('shop/', views.shop, name='shop'),  
    path('delete_cart_item/<int:id>', views.delete_cart_item, name='delete_cart_item'),  

    path('login/', views.login, name='login'), 
    path('register_user/', views.register_user, name='register_user'),
    path('change_password/', views.change_password, name='change_password'),
    path('forgot_password_link/', views.forgot_password_link, name='forgot_password_link'),
    path('password_reset/<str:uid>/<str:token>', views.password_reset, name='password_reset'),
    path('logout/', views.logout, name='logout'),
    path('user_details/<str:user_code>', views.user_details, name='user_details'),
]

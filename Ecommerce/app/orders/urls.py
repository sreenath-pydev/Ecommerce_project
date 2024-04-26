"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from .import views

urlpatterns = [
    path('carts/',views.cart_items,name='cart'),
    path('add_to_cart/<pk>',views.add_to_cart,name='add_to_cart'),
    path('remove_items_from_cart/<pk>',views.remove_items_from_cart,name='remove_items_from_cart'),
    path('place_order/',views.place_order,name='place_order'),
    path('order_status/',views.order_status,name='order_status'),
    path('update_product_quantity_in_cart/',views.update_product_quantity_in_cart,name='update_product_quantity_in_cart'),
    path('payments/',views.payments,name='payments'),
    path('add_address/',views.add_address,name='add_address'),
    path('update_address_form/',views.update_address_form,name='update_address_form'),
    
   
]

from django.urls import path
from .import views

urlpatterns = [
    path('account/',views.account,name='account'),
    path('logout/',views.sing_out,name='logout'),
    
]



from django.shortcuts import render
from .models import products_table
from django.core.paginator import Paginator
# Create your views here.
def product_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    list_products = products_table.objects.all()   
    list_product_paginator = Paginator(list_products,8)
    list_products = list_product_paginator.get_page(page) 
    context = {'list_products':list_products}    
    return render(request,'products.html',context)

def product_details(request):
    return render(request,'product_details.html')
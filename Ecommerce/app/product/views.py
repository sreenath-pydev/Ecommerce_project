from django.shortcuts import render
from .models import products_table
from django.core.paginator import Paginator
# Create your views here.

# home page product listing
def index(request):
    featured_products=products_table.objects.order_by('priority')[:4]
    latest_products=products_table.objects.order_by('-id')[:4]
    context={
        "featured_products":featured_products,
        "latest_products":latest_products
    }
    return render(request,'index.html',context)




# product_list
def product_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    list_products = products_table.objects.all()   
    list_product_paginator = Paginator(list_products,8)
    list_products = list_product_paginator.get_page(page) 
    context = {'list_products':list_products}    
    return render(request,'products.html',context)
# product_details
def product_details(request,pk):
    product= products_table.objects.get(pk=pk)
    related_products=products_table.objects.order_by('-id')[:4]
    context={'product':product,"related_products": related_products}
    return render(request,'product_details.html',context)
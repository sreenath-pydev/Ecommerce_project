from django.shortcuts import render

# Create your views here.
def products(request):
    return render(request,'products.html')

def product_details(request):
    return render(request,'product_details.html')
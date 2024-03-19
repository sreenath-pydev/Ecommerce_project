from django.shortcuts import render

# Create your views here.
def cart_items(request):
    return render(request,'cart.html')
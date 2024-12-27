from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer, Product

# User Creation
def account(request):
    context = {}

    if request.POST and 'register' in request.POST:
        context['register'] = True
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')

        if password != repeat_password:
            messages.error(request, "Passwords do not match.")
        else:
            try:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                Customer.objects.create(user=user, phone=phone, name=username)
                login(request, user)
                return redirect('index')
            except:
                messages.error(request, "Username already taken.")

    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Incorrect username or password.")

    return render(request, 'login-register.html', context)

# Sign Out
def sign_out(request):
    logout(request)
    return redirect('index')

# index
def index(request):
    featured_products = Product.objects.order_by('priority')[:4]
    latest_products = Product.objects.order_by('-id')[:4]
    context = {
        "featured_products": featured_products,
        "latest_products": latest_products,
    }
    return render(request, 'index.html', context)

# Product details
def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.order_by('-id')[:4]
    context = {'product': product, "related_products": related_products}
    return render(request, 'product_details.html', context)

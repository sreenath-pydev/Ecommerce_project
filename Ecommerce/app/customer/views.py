from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import customers
# Create your views here.
def account(request):
    error_massage=None
    if request.POST and 'register' in request.POST:
        print(request.POST)
        
        username=request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        repeat_password=request.POST.get('repeat_password')
        
        if password != repeat_password:
            error_massage="password do not match"
        else:
            try:

        # create user account
                user= User.objects.create_user(
                username=username,
                email=email,
                password=password
                )
        # create customer account
                customer=customers.objects.create(
                user=user,
                phone=phone
                )
                return redirect('index')
            except:
                error_massage='Username Alredy Taken' 

            
    return render(request,'account.html',{'error_massage':error_massage})
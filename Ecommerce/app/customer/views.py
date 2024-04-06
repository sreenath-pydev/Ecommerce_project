from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import customers
# Create your views here.
def account(request):
    context={}

    if request.POST and 'register' in request.POST:
        context['register']=True
        
        username=request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        repeat_password=request.POST.get('repeat_password')
        
        if password != repeat_password:
            error_massage="password do not match"
            messages.error(request,error_massage)
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
                phone=phone,
                name=username,
                )
                
                if user:
                    login(request,user)
                    return redirect('index')  
                
            
            except:
                error_massage='Username Alredy Taken' 
                messages.error(request,error_massage)

     # login request           
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(
            username=username,
            password=password
            )         
        if user:
            login(request,user)
            return redirect('index')  
        else:
            error_massage='Incorrect Username Or password' 
            messages.error(request,error_massage)    
    return render(request,'account.html',context)

def sing_out(request):
    logout(request)
    return redirect('index')
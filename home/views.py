from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')



def welcome(request):
    return render(request,'welcome.html')



# API (METHODS)
# GET ----->     <------- Server 
# POST  ------> Server    
# PUT / Update ------> Update a Data
# Delete  ------> Delete

# Model ---> 

def singup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request,"User Sucessfully Signup")
        return redirect('login')

    return render(request,'singup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect('welcome')
        else:
            messages.error(request,"Invalid User Name and Password")



    return render(request,'login.html')


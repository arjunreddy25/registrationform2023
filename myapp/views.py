from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import CustomUser


# Create your views here.
def Signup(request):
    if request.method== 'POST':
        teamname = request.POST.get('teamname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        my_user = CustomUser.objects.create_user(username=teamname,phone=phone,email=email,password=password)
        my_user.phone = phone
        my_user.save()
        return redirect('login')
      

    return render(request,'signup.html')
 
def Login(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        CustomUser =authenticate(request,email=email,password=password)
        
        if CustomUser is not None:
            Login(request,CustomUser)
            return redirect('next')


    return render(request,'login.html')


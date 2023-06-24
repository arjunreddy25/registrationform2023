from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.
def Signup(request):
    if request.method== 'POST':
        teamname = request.POST('teamname')
        phone = request.POST('phone')
        email = request.POST('email')
        password = request.POST('password')
        
        data = User.objects.create_user(teamname,phone,email,password)
        data.save()
        return redirect('login')

    return render(request,'signup.html')
 
def Login(request):
    if request.method=='POST':
        email = request.POST('email')
        password = request.POST('password')
        user =authenticate(request,email=email,password=password)
        
        if user is not None:
            Login(request,user)
            return redirect('next')

    return render(request,'login.html')


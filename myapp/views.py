from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.
def Signup(request):
    if request.method== 'POST':
        teamname = request.POST.get('teamname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        my_user = User.objects.create_user(teamname=teamname,phone=phone,email=email,password=password)
        my_user.save()
        return redirect('login')
      

    return render(request,'signup.html')
 
def Login(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user =authenticate(request,email=email,password=password)
        
        if user is not None:
            Login(request,user)
            return redirect('next')

    return render(request,'login.html')


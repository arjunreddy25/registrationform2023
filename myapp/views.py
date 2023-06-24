from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def signupview(request):
    if request.method== 'POST':
        teamname = request.POST['teamname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        
        data = User.objects.create_user(teamname=teamname,phone=phone,email=email,password=password)
        data.save()
        return redirect('login')

    return render(request,'signup.html')
 
def Login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email,password=password)
        
        if user is not None:
            auth.login(request,user)
            return render('next')

    return render(request,'login.html')


from ast import Not
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate



# Create your views here.
def index(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method == "POST":
        user_name = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        if password == password2:
            user = User.objects.create_user(username=user_name, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('signin')
        else:
            messages.info(request, 'password does not match')
            return redirect('signup')
    else:
        return render(request, 'authentication/signup.html')

def signin(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['pass1']
        user_check = authenticate(username=user_name, password=password)
        if user_check is not None:
            login(request, user_check)
            f_name = User.first_name
            return render(request, 'authentication/index.html', {'f_name':f_name})
        else:
            messages.info(request, 'invalid credentials')
            return redirect('signin')
    return render(request, 'authentication/signin.html')

def signout(request):
    pass
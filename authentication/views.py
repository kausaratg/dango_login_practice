from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate



# Create your views here.
def index(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        myuser = User.objects.create(username=username, email=email, password=pass1)
        myuser.first_name = f_name
        myuser.last_name = l_name
        myuser.save()
        messages.success(request, "Your Account has been successfully created.")
        return redirect('signin')


    else:
        return render(request, 'authentication/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(Username=username, Password=pass1)
        if user is not None:
            login(request, user)
            f_name = User.first_name
            note = f'Welcome {f_name}'
            return redirect('/')
        else:
            messages.error(request, 'Bad credentials')
            return redirect ('signin')
            
    return render(request, 'authentication/signin.html')

def signout(request):
    pass
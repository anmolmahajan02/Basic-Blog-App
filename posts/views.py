from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username = username):
                messages.info(request,"username already exists")
                return redirect('register') 

            else:
                user =User.objects.create_user(username=username, password=password)
                user.save()
                return redirect("login")
        else:
            messages.info(request,"password does not match")
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        Lusername = request.POST['Lusername']
        Lpassword = request.POST['Lpassword']

        user = auth.authenticate(username = Lusername, password = Lpassword)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, "invalid username or password")
            return redirect('login')
    else:
        return render(request, "login.html")
    
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url="login")
def index(request):
    posts = post.objects.all()
    return render(request, 'index.html',{'posts' : posts})

def post1(request, pk):
    post2 = post.objects.get(id = pk)
    return render(request,"post1.html",{'post' : post2})

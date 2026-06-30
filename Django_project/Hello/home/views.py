from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "your message has been sent successfully")
    return render(request, 'contact.html')

def handleSignup(request):
    if request.method == "POST":
        # Get the post parameters
        Username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if not Username or not pass1 or not pass2:
            messages.error(request, "Please fill out all required fields.")
            return redirect('home')

        if User.objects.filter(username=Username).exists():
            messages.error(request, "Username already exists. Please choose another one.")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('home')

        myuser = User.objects.create_user(Username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not Found")
    
def handleLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST.get('loginusername')
        loginpass = request.POST.get('loginpass')

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('home')

    return HttpResponse("404 - Not Found")



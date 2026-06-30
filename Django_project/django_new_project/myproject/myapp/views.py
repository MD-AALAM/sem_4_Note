from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout


# user authentication password:Majid@2026Secure

# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect('login')  # Redirect to login page if user is not authenticated
    
    return render(request, 'home.html')  # Render the home page for authenticated users

def login(request):
    if request.method == 'POST':
        # Handle login logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            auth_login(request, user)
            return redirect('home')  # Redirect to home page after successful login
    else:
        # No backend authenticated the credentials
        return render(request, 'login.html')
    

    return render(request, 'login.html')
    # return HttpResponse("Hello, World! This is the login page.")

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
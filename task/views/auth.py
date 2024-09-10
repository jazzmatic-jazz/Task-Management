from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from task.models import User, Tasks
from django.utils.safestring import mark_safe


def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username exists
        if not User.objects.filter(email=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('login')
         
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
         
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Email or Password")
            return redirect('login')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('home')
     
    # Render the login page template (GET request)
    return render(request, 'tasks/login.html')


# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        # Check if a user with the provided username already exists
        user = User.objects.filter(email=email)
         
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Email already Exists!")
            return redirect('register')
         
        # Create a new User object with the provided information
        user = User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
         
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
         
        # Display an information message indicating successful account creation
        messages.info(request, mark_safe("Account created Successfully!! <a href='/task/login'>Login Here</a>"))
        return redirect('register')
     
    # Render the registration page template (GET request)
    return render(request, 'tasks/register.html')

 
@login_required
def logout_user(request):
    
    logout(request)
    return render(request, 'tasks/logout.html')
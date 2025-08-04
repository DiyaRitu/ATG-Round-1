from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserForm
from .models import CustomUser


# Home page view — can be a landing page or welcome screen
def home(request):
    return render(request, 'home.html')


# Signup view for new users
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            # Debug: Confirm signup success
            print(f"User {user.username} signed up as {user.user_type}")

            # Redirect to login page instead of logging in automatically
            return redirect('login')
        else:
            # Debug: Show signup form errors
            print("Signup form errors:", form.errors)
    else:
        form = CustomUserForm()
    
    return render(request, 'signup.html', {'form': form})


# Login view for existing users
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Debug: Print user type after login
            print(f"Logged in user type: {user.user_type}")

            # Redirect based on user type
            if user.user_type == 'patient':
                return redirect('patient_dashboard')
            elif user.user_type == 'doctor':
                return redirect('doctor_dashboard')
        else:
            # Debug: Show login form errors in console
            print("Login form errors:", form.errors)
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


# Dashboard for patient users
@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})


# Dashboard for doctor users
@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})

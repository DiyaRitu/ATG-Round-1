from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserForm  
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            # Form is invalid — redisplay with errors
            return render(request, 'signup.html', {'form': form})
    else:
        form = CustomUserForm()
        return render(request, 'signup.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
    
@login_required
def dashboard_view(request):
    if request.user.user_type == 'doctor':
        return render(request, 'doctor_dashboard.html', {'user': request.user})
    else:
        return render(request, 'patient_dashboard.html', {'user': request.user})
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.shortcuts import redirect

def custom_logout_view(request):
    messages.success(request, "You have been logged out.")
    return LogoutView.as_view()(request)


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]

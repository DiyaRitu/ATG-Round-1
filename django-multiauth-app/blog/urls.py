from django.urls import path
from . import views

urlpatterns = [
    path('doctor/create/', views.doctor_blog_create, name='doctor_blog_create'),
    path('doctor/list/', views.doctor_blog_list, name='doctor_blog_list'),
    path('patient/list/', views.patient_blog_list, name='patient_blog_list'),
]

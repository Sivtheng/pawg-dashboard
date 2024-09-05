from django.contrib import admin
from django.urls import path
from myapp import views  # Adjust the import based on your app's name

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('users/', views.list_users, name='list_users'),
    path('contacts/', views.list_contacts, name='list_contacts'),
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('adoption_applications/', views.list_adoption_applications, name='list_adoption_applications'),
    path('login/', views.login, name='login'),
]

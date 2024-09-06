from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('users/', views.list_users, name='list_users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<int:user_id>/update/', views.update_user, name='update_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('contacts/', views.list_contacts, name='list_contacts'),
    path('contacts/create/', views.create_contact, name='create_contact'),
    path('contacts/<int:contact_id>/update/', views.update_contact, name='update_contact'),
    path('contacts/<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('appointments/create/', views.create_appointment, name='create_appointment'),
    path('appointments/<int:appointment_id>/update/', views.update_appointment, name='update_appointment'),
    path('appointments/<int:appointment_id>/delete/', views.delete_appointment, name='delete_appointment'),
    path('adoption_applications/', views.list_adoption_applications, name='list_adoption_applications'),
    path('adoption_applications/create/', views.create_adoption_application, name='create_adoption_application'),
    path('adoption_applications/<int:application_id>/update/', views.update_adoption_application, name='update_adoption_application'),
    path('adoption_applications/<int:application_id>/delete/', views.delete_adoption_application, name='delete_adoption_application'),
]

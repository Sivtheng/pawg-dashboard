from django.urls import path
from . import views

urlpatterns = [
    # User URLs
    path('users/', views.list_users, name='list_users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/update/<int:user_id>/', views.update_user, name='update_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),

    # Contact URLs
    path('contacts/', views.list_contacts, name='list_contacts'),
    path('contacts/create/', views.create_contact, name='create_contact'),
    path('contacts/update/<int:contact_id>/', views.update_contact, name='update_contact'),
    path('contacts/delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),

    # Appointment URLs
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('appointments/create/', views.create_appointment, name='create_appointment'),
    path('appointments/update/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('appointments/delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),

    # Adoption Application URLs
    path('adoption_applications/', views.list_adoption_applications, name='list_adoption_applications'),
    path('adoption_applications/create/', views.create_adoption_application, name='create_adoption_application'),
    path('adoption_applications/update/<int:application_id>/', views.update_adoption_application, name='update_adoption_application'),
    path('adoption_applications/delete/<int:application_id>/', views.delete_adoption_application, name='delete_adoption_application'),

    # Authentication URL
    path('login/', views.login, name='login'),
]

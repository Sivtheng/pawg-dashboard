import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, ContactForm, AppointmentForm, AdoptionApplicationForm, LoginForm

API_BASE_URL = 'http://localhost:8080'

def home(request):
    return render(request, 'home.html') 

# Users Views

def list_users(request):
    response = requests.get(f'{API_BASE_URL}/users')
    if response.status_code == 200:
        users = response.json()
    else:
        users = [] 
    return render(request, 'list_users.html', {'users': users})


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            response = requests.post(f'{API_BASE_URL}/users', json=form.cleaned_data)
            if response.status_code == 201:
                return redirect('list_users')
            else:
                return HttpResponse('Error creating user', status=response.status_code)
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def update_user(request, user_id):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            response = requests.put(f'{API_BASE_URL}/users/{user_id}', json=form.cleaned_data)
            if response.status_code == 200:
                return redirect('list_users')
            else:
                return HttpResponse(f'Error updating user: {response.text}', status=response.status_code)
    else:
        response = requests.get(f'{API_BASE_URL}/users/{user_id}')
        if response.status_code == 200:
            user = response.json()
            form = UserForm(initial=user)
        else:
            form = UserForm()  # Handle the case where the user is not found
    return render(request, 'update_user.html', {'form': form, 'user_id': user_id})


def delete_user(request, user_id):
    if request.method == 'POST':
        response = requests.delete(f'{API_BASE_URL}/users/{user_id}')
        if response.status_code == 204:
            return redirect('list_users')
        else:
            return HttpResponse('Error deleting user', status=response.status_code)
    return render(request, 'delete_user.html', {'user_id': user_id})
    
# Contacts Views

def list_contacts(request):
    response = requests.get(f'{API_BASE_URL}/get_in_touch')
    if response.status_code == 200:
        contacts = response.json()
    else:
        contacts = []
    return render(request, 'list_contacts.html', {'contacts': contacts})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            response = requests.post(f'{API_BASE_URL}/get_in_touch', json=form.cleaned_data)
            if response.status_code == 201:
                return redirect('list_contacts')
            else:
                return HttpResponse('Error creating contact', status=response.status_code)
    else:
        form = ContactForm()
    return render(request, 'create_contact.html', {'form': form})

def update_contact(request, contact_id):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            response = requests.put(f'{API_BASE_URL}/get_in_touch/{contact_id}', json=form.cleaned_data)
            if response.status_code == 200:
                return redirect('list_contacts')
            else:
                return HttpResponse('Error updating contact', status=response.status_code)
    else:
        response = requests.get(f'{API_BASE_URL}/get_in_touch/{contact_id}')
        contact = response.json()
        form = ContactForm(initial=contact)
    return render(request, 'update_contact.html', {'form': form, 'contact_id': contact_id})

def delete_contact(request, contact_id):
    if request.method == 'POST':
        response = requests.delete(f'{API_BASE_URL}/get_in_touch/{contact_id}')
        if response.status_code == 204:
            return redirect('list_contacts')
        else:
            return HttpResponse('Error deleting contact', status=response.status_code)
    return render(request, 'delete_contact.html', {'contact_id': contact_id})

# Appointments Views

def list_appointments(request):
    response = requests.get(f'{API_BASE_URL}/appointments')
    if response.status_code == 200:
        appointments = response.json()
    else:
        appointments = []
    return render(request, 'list_appointments.html', {'appointments': appointments})

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            response = requests.post(f'{API_BASE_URL}/appointments', json=form.cleaned_data)
            if response.status_code == 201:
                return redirect('list_appointments')
            else:
                return HttpResponse('Error creating appointment', status=response.status_code)
    else:
        form = AppointmentForm()
    return render(request, 'create_appointment.html', {'form': form})

def update_appointment(request, appointment_id):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            response = requests.put(f'{API_BASE_URL}/appointments/{appointment_id}', json=form.cleaned_data)
            if response.status_code == 200:
                return redirect('list_appointments')
            else:
                return HttpResponse('Error updating appointment', status=response.status_code)
    else:
        response = requests.get(f'{API_BASE_URL}/appointments/{appointment_id}')
        appointment = response.json()
        form = AppointmentForm(initial=appointment)
    return render(request, 'update_appointment.html', {'form': form, 'appointment_id': appointment_id})

def delete_appointment(request, appointment_id):
    if request.method == 'POST':
        response = requests.delete(f'{API_BASE_URL}/appointments/{appointment_id}')
        if response.status_code == 204:
            return redirect('list_appointments')
        else:
            return HttpResponse('Error deleting appointment', status=response.status_code)
    return render(request, 'delete_appointment.html', {'appointment_id': appointment_id})

# Adoption Applications Views

def list_adoption_applications(request):
    response = requests.get(f'{API_BASE_URL}/adoption_applications')
    if response.status_code == 200:
        applications = response.json()
    else:
        applications = []
    return render(request, 'list_adoption_applications.html', {'applications': applications})

def create_adoption_application(request):
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            response = requests.post(f'{API_BASE_URL}/adoption_applications', json=form.cleaned_data)
            if response.status_code == 201:
                return redirect('list_adoption_applications')
            else:
                return HttpResponse('Error creating adoption application', status=response.status_code)
    else:
        form = AdoptionApplicationForm()
    return render(request, 'create_adoption_application.html', {'form': form})

def update_adoption_application(request, application_id):
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            response = requests.put(f'{API_BASE_URL}/adoption_applications/{application_id}', json=form.cleaned_data)
            if response.status_code == 200:
                return redirect('list_adoption_applications')
            else:
                return HttpResponse('Error updating adoption application', status=response.status_code)
    else:
        response = requests.get(f'{API_BASE_URL}/adoption_applications/{application_id}')
        application = response.json()
        form = AdoptionApplicationForm(initial=application)
    return render(request, 'update_adoption_application.html', {'form': form, 'application_id': application_id})

def delete_adoption_application(request, application_id):
    if request.method == 'POST':
        response = requests.delete(f'{API_BASE_URL}/adoption_applications/{application_id}')
        if response.status_code == 204:
            return redirect('list_adoption_applications')
        else:
            return HttpResponse('Error deleting adoption application', status=response.status_code)
    return render(request, 'delete_adoption_application.html', {'application_id': application_id})

# Authentication View

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            response = requests.post(f'{API_BASE_URL}/login', data=form.cleaned_data)
            if response.status_code == 200:
                # Handle the JWT token received
                # Save token to session or cookies if needed
                return redirect('some_relevant_page')  # Adjust redirect as needed
            else:
                return HttpResponse(f'Error logging in: {response.text}', status=response.status_code)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

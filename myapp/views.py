import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import UserForm, ContactForm, AppointmentForm, AdoptionApplicationForm, LoginForm

API_BASE_URL = 'http://localhost:8080'

def home(request):
    return render(request, 'home.html') 

def get_auth_headers(request):
    token = request.session.get('jwt_token')
    if token:
        return {'Authorization': f'Bearer {token}'}
    return {}

# Users Views

def list_users(request):
    headers = get_auth_headers(request)
    response = requests.get(f'{API_BASE_URL}/users', headers=headers)
    if response.status_code == 200:
        users = response.json()
    else:
        users = []  # Handle error gracefully
    return render(request, 'list_users.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            headers = get_auth_headers(request)
            response = requests.post(f'{API_BASE_URL}/users', json=form.cleaned_data, headers=headers)
            if response.status_code == 201:
                return redirect('list_users')
            else:
                return HttpResponse(f'Error creating user: {response.text}', status=response.status_code)
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def update_user(request, user_id):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            headers = get_auth_headers(request)
            response = requests.put(f'{API_BASE_URL}/users/{user_id}', json=form.cleaned_data, headers=headers)
            if response.status_code == 200:
                return redirect('list_users')
            else:
                return HttpResponse(f'Error updating user: {response.text}', status=response.status_code)
    else:
        response = requests.get(f'{API_BASE_URL}/users/{user_id}', headers=get_auth_headers(request))
        if response.status_code == 200:
            user = response.json()
            form = UserForm(initial=user)
        else:
            form = UserForm()  # Handle error
    return render(request, 'update_user.html', {'form': form, 'user_id': user_id})

def delete_user(request, user_id):
    if request.method == 'POST':
        headers = get_auth_headers(request)
        response = requests.delete(f'{API_BASE_URL}/users/{user_id}', headers=headers)
        if response.status_code == 204:
            return redirect('list_users')
        else:
            return HttpResponse(f'Error deleting user: {response.text}', status=response.status_code)
    return render(request, 'delete_user.html', {'user_id': user_id})
    
# Contacts Views

def list_contacts(request):
    headers = get_auth_headers(request)
    response = requests.get(f'{API_BASE_URL}/get_in_touch', headers=headers)
    if response.status_code == 200:
        contacts = response.json()
    else:
        contacts = []  # Handle error gracefully
    return render(request, 'list_contacts.html', {'contacts': contacts})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            headers = get_auth_headers(request)
            response = requests.post(f'{API_BASE_URL}/get_in_touch', json=form.cleaned_data, headers=headers)
            if response.status_code == 201:
                return redirect('list_contacts')
            else:
                return HttpResponse(f'Error creating contact: {response.text}', status=response.status_code)
    else:
        form = ContactForm()
    return render(request, 'create_contact.html', {'form': form})

def update_contact(request, contact_id):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            headers = get_auth_headers(request)
            response = requests.put(f'{API_BASE_URL}/get_in_touch/{contact_id}', json=form.cleaned_data, headers=headers)
            if response.status_code == 200:
                return redirect('list_contacts')
            else:
                return HttpResponse(f'Error updating contact: {response.text}', status=response.status_code)
    else:
        response = requests.get(f'{API_BASE_URL}/get_in_touch/{contact_id}', headers=get_auth_headers(request))
        if response.status_code == 200:
            contact = response.json()
            form = ContactForm(initial=contact)
        else:
            form = ContactForm()  # Handle error
    return render(request, 'update_contact.html', {'form': form, 'contact_id': contact_id})

def delete_contact(request, contact_id):
    if request.method == 'POST':
        headers = get_auth_headers(request)
        response = requests.delete(f'{API_BASE_URL}/get_in_touch/{contact_id}', headers=headers)
        if response.status_code == 204:
            return redirect('list_contacts')
        else:
            return HttpResponse(f'Error deleting contact: {response.text}', status=response.status_code)
    return render(request, 'delete_contact.html', {'contact_id': contact_id})

# Appointments Views

def list_appointments(request):
    headers = get_auth_headers(request)
    response = requests.get(f'{API_BASE_URL}/appointments', headers=headers)
    if response.status_code == 200:
        appointments = response.json()
    else:
        appointments = []  # Handle error gracefully
    return render(request, 'list_appointments.html', {'appointments': appointments})

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            headers = get_auth_headers(request)
            response = requests.post(f'{API_BASE_URL}/appointments', json=form.cleaned_data, headers=headers)
            if response.status_code == 201:
                return redirect('list_appointments')
            else:
                return HttpResponse(f'Error creating appointment: {response.text}', status=response.status_code)
    else:
        form = AppointmentForm()
    return render(request, 'create_appointment.html', {'form': form})

def update_appointment(request, appointment_id):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            headers = get_auth_headers(request)
            response = requests.put(f'{API_BASE_URL}/appointments/{appointment_id}', json=form.cleaned_data, headers=headers)
            if response.status_code == 200:
                return redirect('list_appointments')
            else:
                return HttpResponse(f'Error updating appointment: {response.text}', status=response.status_code)
    else:
        response = requests.get(f'{API_BASE_URL}/appointments/{appointment_id}', headers=get_auth_headers(request))
        if response.status_code == 200:
            appointment = response.json()
            form = AppointmentForm(initial=appointment)
        else:
            form = AppointmentForm()  # Handle error
    return render(request, 'update_appointment.html', {'form': form, 'appointment_id': appointment_id})

def delete_appointment(request, appointment_id):
    if request.method == 'POST':
        headers = get_auth_headers(request)
        response = requests.delete(f'{API_BASE_URL}/appointments/{appointment_id}', headers=headers)
        if response.status_code == 204:
            return redirect('list_appointments')
        else:
            return HttpResponse(f'Error deleting appointment: {response.text}', status=response.status_code)
    return render(request, 'delete_appointment.html', {'appointment_id': appointment_id})

# Adoption Applications Views

def list_adoption_applications(request):
    headers = get_auth_headers(request)
    response = requests.get(f'{API_BASE_URL}/adoption_applications', headers=headers)
    if response.status_code == 200:
        applications = response.json()
    else:
        applications = []  # Handle error gracefully
    return render(request, 'list_adoption_applications.html', {'applications': applications})

def create_adoption_application(request):
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            headers = get_auth_headers(request)
            response = requests.post(f'{API_BASE_URL}/adoption_applications', json=form.cleaned_data, headers=headers)
            if response.status_code == 201:
                return redirect('list_adoption_applications')
            else:
                return HttpResponse(f'Error creating adoption application: {response.text}', status=response.status_code)
    else:
        form = AdoptionApplicationForm()
    return render(request, 'create_adoption_application.html', {'form': form})

def update_adoption_application(request, application_id):
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            headers = get_auth_headers(request)
            response = requests.put(f'{API_BASE_URL}/adoption_applications/{application_id}', json=form.cleaned_data, headers=headers)
            if response.status_code == 200:
                return redirect('list_adoption_applications')
            else:
                return HttpResponse(f'Error updating adoption application: {response.text}', status=response.status_code)
    else:
        response = requests.get(f'{API_BASE_URL}/adoption_applications/{application_id}', headers=get_auth_headers(request))
        if response.status_code == 200:
            application = response.json()
            form = AdoptionApplicationForm(initial=application)
        else:
            form = AdoptionApplicationForm()  # Handle error
    return render(request, 'update_adoption_application.html', {'form': form, 'application_id': application_id})

def delete_adoption_application(request, application_id):
    if request.method == 'POST':
        headers = get_auth_headers(request)
        response = requests.delete(f'{API_BASE_URL}/adoption_applications/{application_id}', headers=headers)
        if response.status_code == 204:
            return redirect('list_adoption_applications')
        else:
            return HttpResponse(f'Error deleting adoption application: {response.text}', status=response.status_code)
    return render(request, 'delete_adoption_application.html', {'application_id': application_id})

# Authentication View

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            response = requests.post(f'{API_BASE_URL}/login', data=form.cleaned_data)
            if response.status_code == 200:
                # Assuming the response contains the JWT token
                token = response.json().get('token')
                
                # Store token in session or cookies
                request.session['jwt_token'] = token
                
                return redirect('list_users')  # Redirect to a relevant page
            else:
                return HttpResponse(f'Error logging in: {response.text}', status=response.status_code)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


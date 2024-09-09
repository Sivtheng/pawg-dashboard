import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, date, time
import json

from dashboard import settings
from .forms import UserForm, ContactForm, AppointmentForm, AdoptionApplicationForm, LoginForm

API_BASE_URL = 'http://localhost:8080/api'

# Authentication View
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['username'],
                'password': form.cleaned_data['password']
            }
            response = requests.post(f'http://localhost:8080/login', json=data)  # No /api prefix here
            if response.status_code == 200:
                data = response.json()
                request.session['token'] = data['token']  # Store JWT token in session
                request.session['username'] = form.cleaned_data['username']
                return redirect('home')
            else:
                return HttpResponse('Error logging in', status=response.status_code)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        request.session.pop('token', None)
        return redirect('login')
    else:
        return HttpResponse('Invalid request', status=405)

def login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if 'token' not in request.session:
            return redirect(settings.LOGIN_URL)
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@login_required
def home(request):
    username = request.session.get('username', 'User')
    return render(request, 'home.html', {'username': username})

@login_required
def get_auth_headers(request):
    token = request.session.get('token')
    if token:
        return {'Authorization': f'Bearer {token}'}
    return {}

# Users Views
@login_required
def list_users(request):
    headers = get_auth_headers(request)
    response = requests.get(f'{API_BASE_URL}/users', headers=headers)
    if response.status_code == 200:
        users = response.json()
    else:
        users = []  # Handle error gracefully
    return render(request, 'list_users.html', {'users': users})

@login_required
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

@login_required
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

@login_required
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
@login_required
def list_contacts(request):
    headers = get_auth_headers(request)
    response = requests.get(f'{API_BASE_URL}/get_in_touch', headers=headers)
    if response.status_code == 200:
        contacts = response.json()
        return render(request, 'list_contacts.html', {'contacts': contacts})
    else:
        return HttpResponse(f'Error fetching contacts: {response.text}', status=response.status_code)

@login_required
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

@login_required
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

@login_required
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
@login_required
def list_appointments(request):
    headers = get_auth_headers(request)
    response = requests.get(f'{API_BASE_URL}/appointments', headers=headers)
    if response.status_code == 200:
        appointments = response.json()
    else:
        appointments = []  # Handle error gracefully
    return render(request, 'list_appointments.html', {'appointments': appointments})

def serialize_date(date_obj):
    if isinstance(date_obj, datetime):
        return date_obj.isoformat()
    if hasattr(date_obj, 'date'):
        return date_obj.date().isoformat()
    return str(date_obj)

@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Convert date fields to string format
            appointment_data = form.cleaned_data
            appointment_data['appointment_date'] = serialize_date(appointment_data['appointment_date'])
            appointment_data['appointment_time'] = serialize_date(appointment_data['appointment_time'])

            headers = get_auth_headers(request)
            response = requests.post(f'{API_BASE_URL}/appointments', json=appointment_data, headers=headers)
            if response.status_code == 201:
                return redirect('list_appointments')
            else:
                return HttpResponse(f'Error creating appointment: {response.text}', status=response.status_code)
    else:
        form = AppointmentForm()
    return render(request, 'create_appointment.html', {'form': form})

@login_required
def update_appointment(request, appointment_id):
    headers = get_auth_headers(request)  # Get the authentication headers
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Prepare data to update
            updated_data = form.cleaned_data
            
            # Convert date, time, and datetime fields to string format
            for field in ['appointment_date', 'appointment_time']:
                if isinstance(updated_data.get(field), datetime):
                    updated_data[field] = updated_data[field].isoformat()
                elif isinstance(updated_data.get(field), date):
                    updated_data[field] = updated_data[field].isoformat()
                elif isinstance(updated_data.get(field), time):
                    updated_data[field] = updated_data[field].strftime('%H:%M:%S')
            
            response = requests.put(
                f'{API_BASE_URL}/appointments/{appointment_id}',
                data=json.dumps(updated_data),  # Use json.dumps to serialize the data
                headers={**headers, 'Content-Type': 'application/json'}  # Include headers with the PUT request
            )
            if response.status_code == 200:
                return redirect('list_appointments')
            else:
                return HttpResponse(f'Error updating appointment: {response.text}', status=response.status_code)
    else:
        # Fetch current appointment details
        response = requests.get(
            f'{API_BASE_URL}/appointments/{appointment_id}',
            headers=headers  # Include headers with the GET request
        )
        if response.status_code == 200:
            appointment_data = response.json()
            
            # Convert date and time fields back to appropriate format if needed
            # Example parsing if required for form
            form = AppointmentForm(initial=appointment_data)
        else:
            return HttpResponse(f'Error fetching appointment: {response.text}', status=response.status_code)

    return render(request, 'update_appointment.html', {'form': form})


@login_required
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
@login_required
def list_adoption_applications(request):
    headers = get_auth_headers(request)
    response = requests.get(f'{API_BASE_URL}/adoption_applications', headers=headers)
    if response.status_code == 200:
        adoption_applications = response.json()
        return render(request, 'list_adoption_applications.html', {'adoption_applications': adoption_applications})
    else:
        return HttpResponse(f'Error fetching applications: {response.text}', status=response.status_code)

@login_required
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
            print(form.errors)  # Debugging line
    else:
        form = AdoptionApplicationForm()
    return render(request, 'create_adoption_application.html', {'form': form})


@login_required
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

@login_required
def delete_adoption_application(request, application_id):
    if request.method == 'POST':
        headers = get_auth_headers(request)
        response = requests.delete(f'{API_BASE_URL}/adoption_applications/{application_id}', headers=headers)
        if response.status_code == 204:
            return redirect('list_adoption_applications')
        else:
            return HttpResponse(f'Error deleting adoption application: {response.text}', status=response.status_code)
    return render(request, 'delete_adoption_application.html', {'application_id': application_id})

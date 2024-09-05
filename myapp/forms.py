from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20, required=False)
    appointment_date = forms.DateField()
    appointment_time = forms.TimeField()

class AdoptionApplicationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea)
    interest_in_adopting = forms.CharField(max_length=50)
    type_of_animal = forms.CharField(max_length=50)
    special_needs_animal = forms.CharField(max_length=10)
    own_pet_before = forms.CharField(max_length=10)
    working_time = forms.CharField(widget=forms.Textarea)
    living_situation = forms.CharField(widget=forms.Textarea)
    other_animals = forms.CharField(widget=forms.Textarea)
    animal_access = forms.CharField(widget=forms.Textarea)
    travel = forms.CharField(widget=forms.Textarea)
    leave_cambodia = forms.CharField(max_length=10)
    feed = forms.CharField(widget=forms.Textarea)
    anything_else = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

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
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

class AdoptionApplicationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea)
    
    INTEREST_CHOICES = [
        ('fostering', 'Fostering'),
        ('adopting', 'Adopting'),
        ('no_preference', 'No Preference')
    ]
    interest_in_adopting = forms.ChoiceField(choices=INTEREST_CHOICES, widget=forms.RadioSelect)

    ANIMAL_TYPE_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('no_preference', 'No Preference')
    ]
    type_of_animal = forms.ChoiceField(choices=ANIMAL_TYPE_CHOICES, widget=forms.RadioSelect)
    
    SPECIAL_NEEDS_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('maybe', 'No Preference')
    ]
    special_needs_animal = forms.ChoiceField(choices=SPECIAL_NEEDS_CHOICES, widget=forms.RadioSelect)
    
    OWN_PET_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    own_pet_before = forms.ChoiceField(choices=OWN_PET_CHOICES, widget=forms.RadioSelect)
    
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

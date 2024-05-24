from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Patient, Doctor, Pantomogram, Visit, Defect


class PatientRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    date_of_birth = forms.DateField(help_text='YYYY-MM-DD')
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth']

    def save(self, commit=True):
        user = super().save(commit)
        if commit:
            patient = Patient.objects.create(user=user,
                                             date_of_birth=self.cleaned_data['date_of_birth'],
                                             doctor=self.cleaned_data['doctor'])
        return user


class DentistSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit)
        if commit:
            Doctor.objects.create(user=user, phone_number=self.cleaned_data['phone_number'])
        return user


class PatientLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class DoctorLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)




class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['date', 'defect', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class PantomogramForm(forms.ModelForm):
    class Meta:
        model = Pantomogram
        fields = ['file']
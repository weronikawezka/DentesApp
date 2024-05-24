from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import PatientRegisterForm, PatientLoginForm, DoctorLoginForm, DentistSignUpForm, PantomogramForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Patient, Doctor, Visit


def home(request):
    return render(request, 'users/home.html')

def tooths(request):
    return render(request, 'users/tooths.html')

def patient_register(request):
    if request.method == "POST":
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Hi {user.email}, your account was created successfully')
            return redirect('home')
    else:
        form = PatientRegisterForm()
    return render(request, 'users/patient_register.html', {'form': form})


def doctor_register(request):
    if request.method == 'POST':
        form = DentistSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('doctor_profile')
    else:
        form = DentistSignUpForm()
    return render(request, 'users/doctor_register.html', {'form': form})


def patient_login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('patient_profile')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = PatientLoginForm()
    return render(request, 'users/patient_login.html', {'form': form})

def doctor_login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('doctor_profile')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = DoctorLoginForm()
    return render(request, 'users/doctor_login.html', {'form': form})

@login_required
def patient_profile(request):
    patient = request.user.username
    return render(request, 'users/patient_profile.html', {'patient': patient})

@login_required
def doctor_profile(request):
    doctor = request.user.doctor
    return render(request, 'users/doctor_profile.html', {'doctor': doctor})


def profile_links(request):
    patient = request.user.patient
    return render(request, 'users/profile_links.html', {'patient': patient})


def doctor_myprofile(request):
    doctor = request.user.doctor
    return render(request, 'users/doctor_myprofile.html', {'doctor': doctor})

@login_required
def my_patients(request):
    doctor = request.user.doctor
    patients = Patient.objects.filter(doctor=doctor)
    return render(request, 'users/my_patients.html', {'patients': patients})



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient, Visit, Defect
from .forms import VisitForm

@login_required
def add_visit(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.patient = patient
            visit.doctor = request.user.doctor
            visit.save()
            return redirect('my_patients')
    else:
        form = VisitForm()
    return render(request, 'users/add_visit.html', {'form': form, 'patient': patient})







def visits_history(request):
    user = request.user
    patient = Patient.objects.filter(id_patient=user.id).first()
    visits = Visit.objects.filter(id_patient=patient.id_patient) if patient else None
    return render(request, 'users/visits_history.html', {'visits': visits})

def book_appointment(request):
    return render(request, 'users/book_appointment.html')



def upload_pantomogram(request):
    if request.method == 'POST':
        form = PantomogramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')  # Redirect to a success page
    else:
        form = PantomogramForm()
    return render(request, 'users/upload_pantomogram.html', {'form': form})
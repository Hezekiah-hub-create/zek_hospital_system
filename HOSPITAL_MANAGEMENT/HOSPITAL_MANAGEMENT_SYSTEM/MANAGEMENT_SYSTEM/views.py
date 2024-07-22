from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, PatientForm, DoctorForm, AppointmentForm, MedicalRecordForm
from .models import Patient, Doctor, Appointment, MedicalRecord, Profile
from django.contrib import messages

def welcome_view(request):
    return render(request, 'core/welcome.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, user_type=request.POST.get('user_type'))
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request, user_type=None):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    if user_type == 'doctor':
        return render(request, 'core/login_doctor.html', context)
    elif user_type == 'patient':
        return render(request, 'core/login_patient.html', context)
    elif user_type == 'administrator':
        return render(request, 'lcore/ogin_administrator.html', context)
    elif user_type == 'staff':
        return render(request, 'core/login_staff.html', context)
    else:
        return render(request, 'core/login.html', context)


def login_doctor(request):
    return login_view(request)

def login_patient(request):
    return login_view(request)

def login_administrator(request):
    return login_view(request)

def login_staff(request):
    return login_view(request)

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

# Patient views
@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user  # Set the user field
            patient.save()
            messages.success(request, f"Patient {patient.first_name} {patient.last_name} added successfully!")
            return redirect('list_patients')
    else:
        form = PatientForm()
    
    return render(request, 'core/add_patient.html', {'form': form})

@login_required
def list_patients(request):
    patients = Patient.objects.all()
    return render(request, 'core/list_patients.html', {'patients': patients})

@login_required
def update_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('list_patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'core/update_patient.html', {'form': form})

@login_required
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('list_patients')
    return render(request, 'core/delete_patient.html', {'patient': patient})

# Doctor views
@login_required
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user
            doctor.save()
            return redirect('list_doctors')
    else:
        form = DoctorForm()
    return render(request, 'core/add_doctor.html', {'form': form})

@login_required
def list_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'core/list_doctors.html', {'doctors': doctors})

@login_required
def update_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('list_doctors')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'update_doctor.html', {'form': form})

@login_required
def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('list_doctors')
    return render(request, 'core/delete_doctor.html', {'doctor': doctor})

# Appointment views
@login_required
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'core/add_appointment.html', {'form': form})

@login_required
def list_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'core/list_appointments.html', {'appointments': appointments})

@login_required
def update_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('list_appointments')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'core/update_appointment.html', {'form': form})

@login_required
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('list_appointments')
    return render(request, 'core/delete_appointment.html', {'appointment': appointment})

# MedicalRecord views
@login_required
def add_medical_record(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_medical_records')
    else:
        form = MedicalRecordForm()
    return render(request, 'core/add_medical_record.html', {'form': form})

@login_required
def list_medical_records(request):
    medical_records = MedicalRecord.objects.all()
    return render(request, 'core/list_medical_records.html', {'medical_records': medical_records})

@login_required
def update_medical_record(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            return redirect('list_medical_records')
    else:
        form = MedicalRecordForm(instance=medical_record)
    return render(request, 'core/update_medical_record.html', {'form': form})

@login_required
def delete_medical_record(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        medical_record.delete()
        return redirect('list_medical_records')
    return render(request, 'core/delete_medical_record.html', {'medical_record': medical_record})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
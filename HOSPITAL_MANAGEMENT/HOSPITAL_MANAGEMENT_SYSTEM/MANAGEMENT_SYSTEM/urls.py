from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('login/doctor/', views.login_doctor, name='login_doctor'),
    path('login/patient/', views.login_patient, name='login_patient'),
    path('login/administrator/', views.login_administrator, name='login_administrator'),
    path('login/staff/', views.login_staff, name='login_staff'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/', views.list_patients, name='list_patients'),
    path('patients/update/<int:pk>/', views.update_patient, name='update_patient'),
    path('patients/delete/<int:pk>/', views.delete_patient, name='delete_patient'),

    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/', views.list_doctors, name='list_doctors'),
    path('doctors/update/<int:pk>/', views.update_doctor, name='update_doctor'),
    path('doctors/delete/<int:pk>/', views.delete_doctor, name='delete_doctor'),

    path('appointments/add/', views.add_appointment, name='add_appointment'),
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('appointments/update/<int:pk>/', views.update_appointment, name='update_appointment'),
    path('appointments/delete/<int:pk>/', views.delete_appointment, name='delete_appointment'),

    path('medical_records/add/', views.add_medical_record, name='add_medical_record'),
    path('medical_records/', views.list_medical_records, name='list_medical_records'),
    path('medical_records/update/<int:pk>/', views.update_medical_record, name='update_medical_record'),
    path('medical_records/delete/<int:pk>/', views.delete_medical_record, name='delete_medical_record'),

    path('logout/', views.user_logout, name='logout'),
]

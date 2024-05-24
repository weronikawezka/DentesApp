from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('tooths/', views.tooths, name='tooths'),

    path('patient_register/', views.patient_register, name='patient_register'),
    path('patient_login/', views.patient_login, name="patient_login"),
    path('patient_profile/', views.patient_profile, name='patient_profile'),

    path('doctor_register/', views.doctor_register, name='doctor_register'),
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('doctor_profile/', views.doctor_profile, name='doctor_profile'),
    path('doctor_myprofile/', views.doctor_myprofile, name='doctor_myprofile'),
    path('my_patients/', views.my_patients, name='my_patients'),

    path('add_visit/<int:patient_id>/', views.add_visit, name='add_visit'),

    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),

    path('profile_links/', views.profile_links, name='profile_links'),
    path('visits_history/', views.visits_history, name='visits_history'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('upload_pantomogram/', views.upload_pantomogram, name='upload_pantomogram'),

]


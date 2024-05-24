from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.email


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.email

class Tooth(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    tooth_number = models.IntegerField()

    def __str__(self):
        return f"Tooth {self.tooth_number} of Patient {self.patient.user.first_name} {self.patient.user.last_name}"


class Defect(models.Model):
    tooth = models.ForeignKey(Tooth, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Defect {self.name} on Tooth {self.tooth.tooth_number}"

class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    defect = models.ForeignKey(Defect, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Visit for {self.patient.user.first_name} on {self.date}"



class Pantomogram(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    file = models.FileField(upload_to='pantomograms/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



class LogEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_log_entries')
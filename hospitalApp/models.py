from django.db import models
from django.contrib.auth.models import User

class MedicalRecord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    diagnoses = models.TextField(blank=True)
    medications = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    treatment_history = models.TextField(blank=True)

    def __str__(self):
        return f"Medical Record for {self.user.username}"


class UserAuth(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255) 
    email = models.EmailField(max_length=200) # Store password in plain text (NOT RECOMMENDED)

    def __str__(self):
        return self.username
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    
class Appointment(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    doctor = models.CharField(max_length=255)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    user_id = models.IntegerField(default=1)
   
   
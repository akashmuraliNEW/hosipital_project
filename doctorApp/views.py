from django.shortcuts import render
from hospitalApp.models import *

# Create your views here.
def index(request):
    appointments = Appointment.objects.all()

    return render(request, 'doctor/index.html',{'appointments':appointments})
 
def display_medicalHistory(request,id):
   
    try:
        medical_history = MedicalRecord.objects.get(id=id)
        return render(request, 'doctor/display_medicalHistory.html', {'MedicalHistory': medical_history})
    except MedicalRecord.DoesNotExist:
        return render(request, 'doctor/display_medicalHistory.html', {'MedicalHistory': None})
  
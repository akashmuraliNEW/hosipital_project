from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from hospitalApp.models import *

# Create your views here.
def manage_users(request):
    users = User.objects.all()
    departments = Departments.objects.all()
    resources = Resource.objects.all()
    appointments = Appointment.objects.all()

    return render(request, 'admin/index.html', {'users': users,'departments': departments,'resources':resources,'appointments':appointments})

def cancel_appointments(request,id):
    appointments = Appointment.objects.get(id=id)
    appointments.delete()
    return redirect('adminusers')

def create_departments(request):
    if request.method == 'POST':
        department = request.POST['department']
        createdp = Departments.objects.create(name=department)
        createdp.save()
        return redirect('adminusers')
    return render(request, 'admin/create_department.html')

def delete_departments(request,id):
    dp = Departments.objects.get(id=id)
    dp.delete()
    return redirect('adminusers')
def create_resource(request):
    departments = Departments.objects.all()
    resource_types = Resource.RESOURCE_TYPES
    print(resource_types)
    if request.method == 'POST':
        name = request.POST['name']
        resource_type= request.POST['resource_type']
        department_id = request.POST['department']
        department = Departments.objects.get(id=department_id)
        resources = Resource.objects.create(name=name,resource_type=resource_type,department=department)
        resources.save()
        return redirect('adminusers')
    return render(request,'admin/create_resource.html',{'departments': departments,'resource_types': resource_types})
 
def delete_user(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('adminusers')

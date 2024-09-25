from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from .models import *


def medical_history(request,id):
    user = User.objects.get(id=id)
    user_id = id
    medical_record, created = MedicalRecord.objects.get_or_create(user=user)
    if request.method == 'POST':
        medical_record.diagnoses = request.POST['diagnoses']
        medical_record.medications = request.POST['medications']
        medical_record.allergies = request.POST['allergies']
        medical_record.treatment_history = request.POST['treatment_history']
        medical_record.save()
        return redirect('medical',id=user.id)
    
    return render(request, 'user/medical_history.html', {'medical_record': medical_record,'user_id':user_id})

def user_register(request):
    if request.method=='POST':
        email = request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            user = User.objects.create_user(email=email,username=username,password=password)
            user.save()
            return redirect('/')
    return render(request,'user/User_register.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            return render(request,'User_login.html')
    return render(request,'user/User_login.html')
        

def index(request):
    if request.user.is_authenticated:
        user = request.user
        user_id = request.user.id
        user_name = request.user.username
        # print(user_name)

    return render(request,'user/index.html', {'user_id':user_id,'user_name':user_name})
    
def contact(request):
    if request.user.is_authenticated:
        user = request.user
        user_id = request.user.id
            
        
    return render(request,'user/contact.html',{'user_id':user_id})

def about(request):
    if request.user.is_authenticated:
        user = request.user
        user_id = request.user.id
    return render(request,'user/about.html',{'user_id':user_id})

def blog(request):
    if request.user.is_authenticated:
        user = request.user
        user_id = request.user.id
    
    return render(request,'user/blog.html',{'user_id':user_id})

def department(request):
    if request.user.is_authenticated:
        user = request.user
        user_id = request.user.id

    return render(request,'user/department.html',{'user_id':user_id})

def elements(request):
    if request.user.is_authenticated:
        user = request.user
        user_id = request.user.id
    return render(request,'user/doctors.html',{'user_id':user_id})

def single_blog(request):
    return render(request,'user/single-blog.html')

def base(request):
    if request.user.is_authenticated:
        user = request.user   
        user_id = request.user.id
    return render(request,'user/base.html',{'user_id':user_id})

def book_appointment(request):
   
   
   if request.user.is_authenticated:
        user = request.user
        user_id = request.user.id
        
        if request.method =='POST':
            user_id = request.user.id
            name = request.POST['name']
            age = request.POST['age']
            phoneNumber = request.POST['phoneNumber']
            email = request.POST['email']
            doctor = request.POST['doctor']
            appointment_date = request.POST['appointment_date']
            appointment_time = request.POST['appointment_time']
            appointment = Appointment(
            name=name,
            age=age,
            phoneNumber=phoneNumber,
            email=email,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            user_id=user_id
        )
            appointment.save()
            # return redirect('/')
   return render(request,'user/book _appointment.html',{'user_id':user_id})


def health_tips(request):
    if request.user.is_authenticated:
        user = request.user   
        user_id = request.user.id
    return render(request,'user/health_tips.html',{'user_id':user_id})


"""hospitalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from hospitalApp import views
from adminApp import views as adminViews

urlpatterns = [
    path('admins/', admin.site.urls),
    path('home', views.index,name='index'),
    path('contact/', views.contact,name='contact'),
    path('about/', views.about,name='about'),
    path('elements/', views.elements,name='elements'),
    path('department/', views.department,name='department'),
    path('blog/', views.blog,name='blog'),
    path('single_blog/', views.single_blog,name='single-blog'),
    path('register/', views.user_register,name='login'),
    path('medical/<int:id>', views.medical_history,name='medical'),
    path('', views.user_login,name='user_login'),
    path('base', views.base,name='base'),
    path('appointment', views.book_appointment,name='appointment'),
    path('health_tips', views.health_tips,name='health_tips'),
   
    # admin urls
    path('adminusers', adminViews.manage_users,name='adminusers'),
    path('create_department', adminViews.create_departments,name='create_departments'),
    path('delete_departments/<int:id>', adminViews.delete_departments,name='delete_departments'),
    path('create_resource', adminViews.create_resource,name='create_resource'),
    path('cancel_appointments/<int:id>', adminViews.cancel_appointments,name='cancel_appointments'),\
    path('delete_user<int:id>',adminViews.delete_user , name='delete_user'),
    


    # doctor url
    
    path('', include('doctorApp.urls')),

    

]

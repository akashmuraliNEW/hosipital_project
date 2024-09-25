from django.urls import path
from . import views


urlpatterns = [
    path('doctors',views.index,name='doctors'),
    path('display_medicalHistory/<int:id>',views.display_medicalHistory,name='display_medicalHistory'),
]
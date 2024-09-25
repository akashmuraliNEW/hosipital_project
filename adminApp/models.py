from django.db import models

# Create your models here.
class Departments(models.Model):
    name = models.CharField(max_length=255)

class Resource(models.Model):
    RESOURCE_TYPES = [
        ('MEDICAL_EQUIPMENT', 'Medical Equipment'),
        ('PERSONNEL', 'Personnel'),
        ('FACILITIES', 'Facilities'),
        ('SUPPLIES', 'Supplies'),
        ('TRANSPORTATION', 'Transportation'),
    ]

    name = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
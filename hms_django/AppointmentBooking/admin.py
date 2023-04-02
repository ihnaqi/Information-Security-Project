from django.contrib import admin
from .models import  Department,Appointment, Prescription
# Register your models here.
admin.site.register(Department)

admin.site.register(Appointment)

admin.site.register(Prescription)

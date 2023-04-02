import json
import os
from django.db import models
import datetime
from datetime import date,datetime
from datetime import timedelta
from django.db.models import Sum
from UserSystem.models import Doctor, Patient
from rest_framework import serializers
from django.utils import timezone



class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name=models.CharField(max_length=255)
    department_location = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='patient')
    # date = models.DateField(default=timezone.now().date)
    # time = models.TimeField(default='09:00')
    #date = models.DateField()
    #time = models.TimeField()
    #date=models.ForeignKey(Date,on_delete=models.CASCADE,related_name='date')
    #time=models.ForeignKey(Time,on_delete=models.CASCADE,related_name='time')
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='doctor')
    description=models.CharField(max_length=255)
   
    def __str__(self):
         return self.description + " - "  + self.patient.user.name + " - Dr. " + self.doctor.user.name


class Prescription(models.Model):
    prescription_id=models.AutoField(primary_key=True)
    # patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    appointment_id = models.ForeignKey(Appointment,on_delete=models.CASCADE, default=None)
    # doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return "Prescription"
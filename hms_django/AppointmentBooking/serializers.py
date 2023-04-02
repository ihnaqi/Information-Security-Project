from rest_framework import serializers
from .models import  Prescription,Department,Appointment




class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ('prescription_id',
   'appointment',
    'medicines')


class MedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('medicines_id',
        'medicines_qty',
        'medicines_name' )


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_id',
    'department_name',
    'department_location' )


class AppointmentSerializer(serializers.ModelSerializer):
    
    # patient = serializers.StringRelatedField(many=False)
    # doctor = serializers.StringRelatedField(many=False)

    class Meta:
        model = Appointment
        fields = ('appointment_id',
                'patient',
                'doctor',
                'description',
                'date',
                'time'
                )

class GetAppointmentSerializer(serializers.ModelSerializer):
    
    patient = serializers.StringRelatedField(many=False)
    doctor = serializers.StringRelatedField(many=False)

    class Meta:
        model = Appointment
        fields = ('appointment_id',
                'patient',
                'doctor',
                'description'
                )


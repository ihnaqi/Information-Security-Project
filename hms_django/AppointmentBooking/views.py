import json
import string
from django.http import response
from django.urls import reverse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .serializers import  AppointmentSerializer,  DepartmentSerializer, GetAppointmentSerializer,  MedicinesSerializer, PrescriptionSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import HttpResponse
from UserSystem.models import Patient
from .models import Appointment,   Department, Prescription
from itertools import chain
from operator import attrgetter



#Department

@api_view(['GET', 'POST']) #Post for new
def departments_list(request):
    if request.method == 'GET':
        department = Department.objects.all()
        department_name_keyword = request.GET.get('department_name_keyword', None)
        if department_name_keyword is not None:
            department = department.filter(department_name__icontains=department_name_keyword)
        
        department_serializer = DepartmentSerializer(department, many=True)
        return JsonResponse(department_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse(department_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(department_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
@api_view(['GET','PUT','DELETE'])
def departments_detail(request, pk):  
    try: 
        department = Department.objects.get(pk=pk) 
    except Department.DoesNotExist: 
        return JsonResponse({'message': 'The Department does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        department_serializer = DepartmentSerializer(department) 
        return JsonResponse(department_serializer.data) 

    elif request.method == 'PUT': 
        department_data = JSONParser().parse(request) 
        department_serializer = DepartmentSerializer(department, data=department_data) 
        if department_serializer.is_valid(): 
            department_serializer.save() 
            return JsonResponse(department_serializer.data) 
        return JsonResponse(department_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        department.delete() 
        return JsonResponse({'message': 'Department was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


#Appointment

@api_view(['GET', 'POST']) #Post for new
def appointments_list(request):
    if request.method == 'GET':
        appointment = Appointment.objects.all()
        appointment_name_keyword = request.GET.get('appointment_name_keyword', None)
        if appointment_name_keyword is not None:
            appointment = appointment.filter(appointment_name__icontains=appointment_name_keyword)
        
        appointment_serializer = GetAppointmentSerializer(appointment, many=True)
        return JsonResponse(appointment_serializer.data, safe=False)

    elif request.method == 'POST':
        appointment_data = JSONParser().parse(request)
        user_id = appointment_data['patient']
        try: 
            patient = Patient.objects.get(user=user_id) 
            print(patient.user.name)
            appointment_data['patient']=patient.pk
        except Patient.DoesNotExist: 
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
  
        print(appointment_data)

        appointment_serializer = AppointmentSerializer(data=appointment_data)
        # patient_id = appointment_serializer.
        
        if appointment_serializer.is_valid():
            appointment_serializer.save()
            return JsonResponse(appointment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
@api_view(['GET','PUT','DELETE'])
def appointments_detail(request, pk):  
    try: 
        appointment = Appointment.objects.get(pk=pk) 
    except Appointment.DoesNotExist: 
        return JsonResponse({'message': 'The Appointment does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        appointment_serializer = AppointmentSerializer(appointment) 
        return JsonResponse(appointment_serializer.data) 

    elif request.method == 'PUT': 
        appointment_data = JSONParser().parse(request) 
        appointment_serializer = AppointmentSerializer(appointment, data=appointment_data) 
        if appointment_serializer.is_valid(): 
            appointment_serializer.save() 
            return JsonResponse(appointment_serializer.data) 
        return JsonResponse(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        appointment.delete() 
        return JsonResponse({'message': 'Appointment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def appointmentsByPatient(request, pk):  
    if request.method == 'GET':
        patient = Patient.objects.get(user=pk) 
        patient=Patient.objects.get(pk=patient.pk)
        appointment = Appointment.objects.filter(patient=patient)
        appointment_name_keyword = request.GET.get('appointment_name_keyword', None)
        if appointment_name_keyword is not None:
            appointment = appointment.filter(appointment_name__icontains=appointment_name_keyword)
        
        appointment_serializer = GetAppointmentSerializer(appointment, many=True)
        return JsonResponse(appointment_serializer.data, safe=False)
    
        
        
        
    elif request.method == 'POST':
        appointment_data = JSONParser().parse(request)
        appointment_serializer = AppointmentSerializer(data=appointment_data)
        if appointment_serializer.is_valid():
            appointment_serializer.save()
            return JsonResponse(appointment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 

#Prescriptions

@api_view(['GET', 'POST']) #Post for new
def prescriptions_list(request):
    if request.method == 'GET':
        prescription = Prescription.objects.all()
        prescription_name_keyword = request.GET.get('prescription_name_keyword', None)
        if prescription_name_keyword is not None:
            prescription = prescription.filter(prescription_name__icontains=prescription_name_keyword)
        
        prescription_serializer = PrescriptionSerializer(prescription, many=True)
        return JsonResponse(prescription_serializer.data, safe=False)

    elif request.method == 'POST':
        prescription_data = JSONParser().parse(request)
        prescription_serializer = PrescriptionSerializer(data=prescription_data)
        if prescription_serializer.is_valid():
            prescription_serializer.save()
            return JsonResponse(prescription_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(prescription_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
@api_view(['GET','PUT','DELETE'])
def prescriptions_detail(request, pk):  
    try: 
        prescription = Prescription.objects.get(pk=pk) 
    except Prescription.DoesNotExist: 
        return JsonResponse({'message': 'The Prescription does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        prescription_serializer = PrescriptionSerializer(prescription) 
        return JsonResponse(prescription_serializer.data) 

    elif request.method == 'PUT': 
        prescription_data = JSONParser().parse(request) 
        prescription_serializer = PrescriptionSerializer(prescription, data=prescription_data) 
        if prescription_serializer.is_valid(): 
            prescription_serializer.save() 
            return JsonResponse(prescription_serializer.data) 
        return JsonResponse(prescription_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        prescription.delete() 
        return JsonResponse({'message': 'Prescription was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# Homepage
def Clients_Landing(request):
    # # ClientsList = Client.objects.all()
    # params = {'ClientsList':ClientsList}
    # return render(request,'Clients_Landing.html',params)
    return HttpResponse("")

def Clients_View(request):
    return HttpResponse("")


@api_view(['GET'])
def clients_summary(request, pk):  
    try: 
        client = Client.objects.get(pk=pk) 
    except Client.DoesNotExist: 
        return JsonResponse({'message': 'The Client does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        return JsonResponse(
            {"client_name":client.client_name,
            "get_one_month": client.get_one_month(),
            "get_two_month" : client.get_two_month(),
            "get_three_month":client.get_three_month(),
            "get_four_month":client.get_four_month(),
            "get_total":client.get_total()
            },safe=False)



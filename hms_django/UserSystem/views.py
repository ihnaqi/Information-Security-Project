from rest_framework import generics,permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from UserSystem.models import Doctor, User,Patient
from .serializers import PatientSerializer, DoctorSerializer, UserSerializer,PatientSignupSerializer, DoctorSignupSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .permissions import IsPatientUser, IsDoctorUser
from . import views

from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from django.http.response import JsonResponse

class PatientSignupView(generics.GenericAPIView):
    serializer_class=PatientSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response ({"user": UserSerializer(user, context= self.get_serializer_context()).data,
        "token": Token.objects.get(user=user).key, 
        "message": "Account created successfully"})
    



class DoctorSignupView(generics.GenericAPIView):
    serializer_class=DoctorSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response ({"user": UserSerializer(user, context= self.get_serializer_context()).data,
        "token": Token.objects.get(user=user).key, 
        "message": "Account created successfully"})

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data,
        context = {'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        print(token.key, user.pk, user.is_patient)
        return Response({
        'token': token.key,
        'user_id': user.pk,
        'is_patient': user.is_patient,
        })

        

class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)

class PatientOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsPatientUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class DoctorOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsDoctorUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user


@api_view(['GET', 'POST']) #Post for new
def doctors_list(request):
    if request.method == 'GET':
        doctor = Doctor.objects.all()
        doctor_name_keyword = request.GET.get('doctor_name_keyword', None)
        if doctor_name_keyword is not None:
            doctor = doctor.filter(doctor_name__icontains=doctor_name_keyword)
        
        doctor_serializer = DoctorSerializer(doctor, many=True)
        return JsonResponse(doctor_serializer.data, safe=False)

    elif request.method == 'POST':
        doctor_data = JSONParser().parse(request)
        doctor_serializer = DoctorSerializer(data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse(doctor_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
@api_view(['GET','PUT','DELETE'])
def doctors_detail(request, pk):  
    try: 
        doctor = Doctor.objects.get(pk=pk) 
    except Doctor.DoesNotExist: 
        return JsonResponse({'message': 'The Doctor does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        doctor_serializer = DoctorSerializer(doctor) 
        return JsonResponse(doctor_serializer.data) 

    elif request.method == 'PUT': 
        doctor_data = JSONParser().parse(request) 
        doctor_serializer = DoctorSerializer(doctor, data=doctor_data) 
        if doctor_serializer.is_valid(): 
            doctor_serializer.save() 
            return JsonResponse(doctor_serializer.data) 
        return JsonResponse(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        doctor.delete() 
        return JsonResponse({'message': 'Doctor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST']) #Post for new
def patients_list(request):
    if request.method == 'GET':
        patient = Patient.objects.all()
        patient_name_keyword = request.GET.get('patient_name_keyword', None)
        if patient_name_keyword is not None:
            patient = patient.filter(patient_name__icontains=patient_name_keyword)
        
        patient_serializer = PatientSerializer(patient, many=True)
        return JsonResponse(patient_serializer.data, safe=False)

    elif request.method == 'POST':
        patient_data = JSONParser().parse(request)
        patient_serializer = PatientSerializer(data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse(patient_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
@api_view(['GET','PUT','DELETE'])
def patients_detail(request, pk):  
    try: 
        patient = Patient.objects.get(pk=pk) 
    except Patient.DoesNotExist: 
        return JsonResponse({'message': 'The Patient does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        patient_serializer = PatientSerializer(patient) 
        return JsonResponse(patient_serializer.data) 

    elif request.method == 'PUT': 
        patient_data = JSONParser().parse(request) 
        patient_serializer = PatientSerializer(patient, data=patient_data) 
        if patient_serializer.is_valid(): 
            patient_serializer.save() 
            return JsonResponse(patient_serializer.data) 
        return JsonResponse(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        patient.delete() 
        return JsonResponse({'message': 'Patient was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


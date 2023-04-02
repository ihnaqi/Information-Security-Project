from  django.urls import path
from .views import PatientSignupView,doctors_list,doctors_detail, DoctorSignupView,CustomAuthToken, LogoutView, PatientOnlyView, DoctorOnlyView
from . import views

from django.conf.urls import url

urlpatterns = [

    path('signup/patient/', PatientSignupView.as_view()),
    path('signup/doctor/', DoctorSignupView.as_view()),

    #LOGIN/LOGOUT
    path('login/', CustomAuthToken.as_view(), name='auth_token'),
    path('logout/', LogoutView.as_view()),

    path('patient/dashboard', PatientOnlyView.as_view()),
    path('doctor/dashboard', DoctorOnlyView.as_view()),

    url(r'Doctors$', views.doctors_list),
    url(r'Doctors/(?P<pk>[0-9]+)$', views.doctors_detail),

    url(r'Patients$', views.patients_list),
    url(r'Patients/(?P<pk>[0-9]+)$', views.patients_detail),



]
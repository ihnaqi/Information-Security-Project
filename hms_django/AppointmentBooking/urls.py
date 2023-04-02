
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

#Department
url(r'^api/Departments$', views.departments_list),
url(r'^api/Departments/(?P<pk>[0-9]+)$', views.departments_detail),


#Appointment
url(r'^api/Appointments$', views.appointments_list),
url(r'^api/Appointments/(?P<pk>[0-9]+)$', views.appointments_detail),
url(r'^api/AppointmentsByPatient/(?P<pk>[0-9]+)$', views.appointmentsByPatient),


#Prescription
url(r'^api/Prescriptions$', views.prescriptions_list),
url(r'^api/Prescriptions/(?P<pk>[0-9]+)$', views.prescriptions_detail),

path('', views.Clients_Landing, name='Clients_Landing'),
path('Clients_View/<int:id>/', views.Clients_View, name='Clients_View'),

]


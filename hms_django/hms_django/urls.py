

from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path,include
from . import view

urlpatterns = [

    url(r'^', include('AppointmentBooking.urls')),

    path('api/', include('UserSystem.urls')),

    path('admin/', admin.site.urls),

    
    #Default
    path('', view.index, name='index'),

]

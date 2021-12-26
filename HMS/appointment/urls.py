from django.urls import path
from .import views



urlpatterns = [

   
    path('send_email', views.send_email.as_view(), name="send_email"),
    path('appointment', views.appointment.as_view(), name="appointment"),
    path('manage_appointment', views.manage_appointment.as_view(), name="manage_appointment"),
    path('our_appointments', views.our_appointments.as_view(), name="our_appointments"),

    
]
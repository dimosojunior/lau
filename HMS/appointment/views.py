from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from hospital.models import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from hospital.forms import * 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db.models import Q
import datetime
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.conf import settings

from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string, get_template
# Create your views here.
class send_email(TemplateView):
	template_name = 'appointment/send_email.html'

	def post(self, request):
		fname = request.POST.get('fname')
		sname = request.POST.get('sname')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')

		email = EmailMessage(
			subject = f"{fname} from doctor family",
			body = message,
			from_email = settings.EMAIL_HOST_USER,
			to = [settings.EMAIL_HOST_USER],
			reply_to=[email]


			)

		email.send()
		messages.add_message(request, messages.SUCCESS, f"Thanks {fname}, you have successed to send an email to us")
		return HttpResponseRedirect(request.path)
		
    
    #return render(request, 'appointment/appointment_home.html')


class appointment(TemplateView):
	template_name = 'appointment/appointment.html'

	def post(self, request):
		fname = request.POST.get('fname')
		sname = request.POST.get('sname')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')

		appointment = Appointment.objects.create(
			fname = fname,
			sname = sname,
			email = email,
			phone = phone,
			message = message,


			)
		appointment.save()

		messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment")
		return HttpResponseRedirect(request.path)

class manage_appointment(TemplateView):
	template_name = 'appointment/manage_appointment.html'

	def post(self, request):
		date = request.POST.get("date")

		appointment_id = request.POST.get("appointment-id")
		appointment = Appointment.objects.get(id=appointment_id)
		appointment.accepted =True
		appointment.accepted_tarehe = datetime.datetime.now()
		appointment.save()

		#data = {
		  #  "fname":appointment.fname,
		   # "date":date,


		#}
		#message = get_template('appointment/email.html').render(data)
		#email = EmailMessage(
			#"Abot Your Appointment",
			#message,
			#settings.EMAIL_HOST_USER,
			#[appointment.email],

			#)
		#email.content_subtype = 'html'
		#email.send()

		messages.add_message(request, messages.SUCCESS, f"you are accepted an appointment of {appointment.fname} {appointment.sname} on {date}")
		return HttpResponseRedirect(request.path)

	def get_context_data(self,*args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		appointments = Appointment.objects.all()

		context.update({
			"appointments":appointments,
			"title":"Manage Appointment"

		})
		return context


class our_appointments(TemplateView):
	template_name = 'appointment/our_appointments_email.html'
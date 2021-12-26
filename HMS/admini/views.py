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


# Create your views here.
def index(response):
    all_appointments = Appointment.objects.filter(accepted=False).order_by('-id')
    

    context = {
        
        "all_appointments":all_appointments
    }
    
    return render(response, 'admini/index.html',context)

class list_watoto_dozi(ListView):
    model = Dozi
    template_name = 'admini/list_watoto_dozi.html'
    context_object_name = 'watoto'
    

    def get_queryset(self):
        return Dozi.objects.order_by('-id')

class watoto_dozi_view(DetailView):
	model = Dozi
	template_name = 'admini/watoto_dozi_view.html'


class update_watoto_dozi(SuccessMessageMixin, UpdateView):
    model = Dozi
    template_name = 'hospital/add_dozi.html'
    form_class = DoziForm
    success_url = reverse_lazy('list_watoto_dozi')
    success_message = "Data Updated Successfully"

def delete_watoto_dozi(request, pk):
    watoto = get_object_or_404(Dozi, id=pk)
    watoto.delete()
    return redirect('list_watoto_dozi')

'''
def search_watoto_dozi(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(name__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    watoto = Dozi.objects.filter(search)
    mylist= []
    mylist += [x.name for x in watoto]
    return JsonResponse(mylist, safe=False)
'''

#KWA AJILI YA WAZEEE ZINAANZIA HAPA
class list_wazee_dozi(ListView):
    model = WazeeDozi
    template_name = 'admini/list_wazee_dozi.html'
    context_object_name = 'wazee'
    

    def get_queryset(self):
        return WazeeDozi.objects.order_by('-id')

class wazee_dozi_view(DetailView):
	model = WazeeDozi
	template_name = 'admini/wazee_dozi_view.html'


class update_wazee_dozi(SuccessMessageMixin, UpdateView):
    model = WazeeDozi
    template_name = 'hospital/add_dozi_wazee.html'
    form_class = WazeeDoziForm
    success_url = reverse_lazy('list_wazee_dozi')
    success_message = "Data Updated Successfully"

def delete_wazee_dozi(request, pk):
    wazee = get_object_or_404(WazeeDozi, id=pk)
    wazee.delete()
    return redirect('list_wazee_dozi')


   #ZA WAZEE ZINAISHIA HAPA


   #ZA WAGONJWA WA KAWAIDA ZINAANZIA HAPA
class list_kawaida_dozi(ListView):
    model = KawaidaDozi
    template_name = 'admini/list_kawaida_dozi.html'
    context_object_name = 'kawaida'
    

    def get_queryset(self):
        return KawaidaDozi.objects.order_by('-id')

class kawaida_dozi_view(DetailView):
	model = KawaidaDozi
	template_name = 'admini/kawaida_dozi_view.html'


class update_kawaida_dozi(SuccessMessageMixin, UpdateView):
    model = KawaidaDozi
    template_name = 'hospital/add_dozi_kawaida.html'
    form_class = KawaidaDoziForm
    success_url = reverse_lazy('list_kawaida_dozi')
    success_message = "Data Updated Successfully"

def delete_kawaida_dozi(request, pk):
    kawaida = get_object_or_404(KawaidaDozi, id=pk)
    kawaida.delete()
    return redirect('list_kawaida_dozi')


   #ZINAISHIA HAPA ZA KAWAIDA


  #HIZI NI KWA AJILI YA WAJAWAZITO ZINAANZIA HAPA

class list_wajawazito_dozi(ListView):
    model = WajawazitoDozi
    template_name = 'admini/list_wajawazito_dozi.html'
    context_object_name = 'wajawazito'
    

    def get_queryset(self):
        return WajawazitoDozi.objects.order_by('-id')

class wajawazito_dozi_view(DetailView):
	model = WajawazitoDozi
	template_name = 'admini/wajawazito_dozi_view.html'


class update_wajawazito_dozi(SuccessMessageMixin, UpdateView):
    model = WajawazitoDozi
    template_name = 'hospital/add_dozi_wajawazito.html'
    form_class = WajawazitoDoziForm
    success_url = reverse_lazy('list_wajawazito_dozi')
    success_message = "Data Updated Successfully"

def delete_wajawazito_dozi(request, pk):
    wajawazito = get_object_or_404(WajawazitoDozi, id=pk)
    wajawazito.delete()
    return redirect('list_wajawazito_dozi')



#SASA ZINAZOANZA HAPA NI KWA AJILI YA VIPIMO TU

#HIZI NI KWA AJILI YA VIPIMO VYA WATOTO
class list_watoto_vipimo(ListView):
    model = Vipimo
    template_name = 'admini/list_watoto_vipimo.html'
    context_object_name = 'watoto'
    

    def get_queryset(self):
        return Vipimo.objects.order_by('-id')

class watoto_vipimo_view(DetailView):
	model = Vipimo
	template_name = 'admini/watoto_vipimo_view.html'


class update_watoto_vipimo(SuccessMessageMixin, UpdateView):
    model = Vipimo
    template_name = 'hospital/add_kipimo.html'
    form_class = VipimoForm
    success_url = reverse_lazy('list_watoto_vipimo')
    success_message = "Data Updated Successfully"

def delete_watoto_vipimo(request, pk):
    watoto = get_object_or_404(Vipimo, id=pk)
    watoto.delete()
    return redirect('list_watoto_vipimo')



#KWA AJILI YA WAZEEE ZINAANZIA HAPA
class list_wazee_vipimo(ListView):
    model = WazeeVipimo
    template_name = 'admini/list_wazee_vipimo.html'
    context_object_name = 'wazee'
    

    def get_queryset(self):
        return WazeeVipimo.objects.order_by('-id')

class wazee_vipimo_view(DetailView):
	model = WazeeVipimo
	template_name = 'admini/wazee_vipimo_view.html'


class update_wazee_vipimo(SuccessMessageMixin, UpdateView):
    model = WazeeVipimo
    template_name = 'hospital/add_kipimo_wazee.html'
    form_class = WazeeVipimoForm
    success_url = reverse_lazy('list_wazee_vipimo')
    success_message = "Data Updated Successfully"

def delete_wazee_vipimo(request, pk):
    wazee = get_object_or_404(WazeeVipimo, id=pk)
    wazee.delete()
    return redirect('list_wazee_vipimo')


   #ZA WAZEE ZINAISHIA HAPA



#ZA WAGONJWA WA KAWAIDA ZINAANZIA HAPA
class list_kawaida_vipimo(ListView):
    model = KawaidaVipimo
    template_name = 'admini/list_kawaida_vipimo.html'
    context_object_name = 'kawaida'
    

    def get_queryset(self):
        return KawaidaVipimo.objects.order_by('-id')

class kawaida_vipimo_view(DetailView):
	model = KawaidaVipimo
	template_name = 'admini/kawaida_vipimo_view.html'


class update_kawaida_vipimo(SuccessMessageMixin, UpdateView):
    model = KawaidaVipimo
    template_name = 'hospital/add_kipimo_kawaida.html'
    form_class = KawaidaVipimoForm
    success_url = reverse_lazy('list_kawaida_vipimo')
    success_message = "Data Updated Successfully"

def delete_kawaida_vipimo(request, pk):
    kawaida = get_object_or_404(KawaidaVipimo, id=pk)
    kawaida.delete()
    return redirect('list_kawaida_vipimo')


   #ZINAISHIA HAPA ZA KAWAIDA



#HIZI NI KWA AJILI YA WAJAWAZITO ZINAANZIA HAPA

class list_wajawazito_vipimo(ListView):
    model = WajawazitoVipimo
    template_name = 'admini/list_wajawazito_vipimo.html'
    context_object_name = 'wajawazito'
    

    def get_queryset(self):
        return WajawazitoVipimo.objects.order_by('-id')

class wajawazito_vipimo_view(DetailView):
	model = WajawazitoVipimo
	template_name = 'admini/wajawazito_vipimo_view.html'


class update_wajawazito_vipimo(SuccessMessageMixin, UpdateView):
    model = WajawazitoVipimo
    template_name = 'hospital/add_kipimo_wajawazito.html'
    form_class = WajawazitoVipimoForm
    success_url = reverse_lazy('list_wajawazito_vipimo')
    success_message = "Data Updated Successfully"

def delete_wajawazito_vipimo(request, pk):
    wajawazito = get_object_or_404(WajawazitoVipimo, id=pk)
    wajawazito.delete()
    return redirect('list_wajawazito_vipimo')


#MWISHO WA YOTE NI HAPO


def all_time_payment(request):
    
    payment = KawaidaDozi.objects.filter(paid=True).order_by('-id')
    

    context = {
        
        "payment":payment
    }

    return render(request, 'admini/all_time_payment.html', context)


def today_payment(request):

	start_date = datetime.date(2021,10,13)
	end_date = datetime.date(2021,12,30)

	myDate = datetime.datetime.now()
	myDate1 = datetime.datetime.now().date()
	myDate2 = datetime.datetime.now().time()

	payment = KawaidaDozi.objects.filter(paid=True).order_by('-id')

    
    

	context = {
	    
	    "payment":payment,
	    "myDate":myDate,
	    "myDate1":myDate1,
	    "myDate2":myDate2
	}

	return render(request, 'admini/today_payment.html', context)

'''
def available_medicines(request):

	

	available_medicines = AvailableMedicines.objects.all().order_by('-id')

    
    

	context = {
	    
	    
	    "available_medicines":available_medicines
	}

	return render(request, 'admini/all_available_medicines.html', context)
'''
def available_medicines(request):
    title = 'List of Dozi'
    
    available_medicines = AvailableMedicines.objects.all().order_by('-id')
    form = AvailableMedicinesForm(request.POST or None)# form ya kuserch ila nimeifuta nimetumia hzo code za chini

    #context = {
        #"title":title,
        #"available_medicines":available_medicines,
        #"form":form
    #}
    #searching button codes
    if request.method == 'POST':
        available_medicines = AvailableMedicines.objects.filter( medicine_name__icontains=form['medicine_name'].value())

    context = {
        "form":form,
        "title":title,
        "available_medicines":available_medicines
    }

    return render(request, 'admini/all_available_medicines.html', context)

class add_available_medicines(SuccessMessageMixin, CreateView):
    model = AvailableMedicines
    template_name = 'admini/add_available_medicines.html'
    form_class = AvailableMedicinesForm
    success_url = reverse_lazy('available_medicines')
    success_message = "Medicines Added Successfully"


class update_available_medicines(SuccessMessageMixin, UpdateView):
    model = AvailableMedicines
    template_name = 'admini/add_available_medicines.html'
    form_class = AvailableMedicinesForm
    success_url = reverse_lazy('available_medicines')
    success_message = "Data Updated Successfully"

def delete_available_medicines(request, pk):
    medicine = get_object_or_404(AvailableMedicines, id=pk)
    medicine.delete()
    return redirect('available_medicines')

def search_available_medicines(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(medicine_name__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    available_medicines = AvailableMedicines.objects.filter(search)
    mylist= []
    mylist += [x.medicine_name for x in available_medicines]
    return JsonResponse(mylist, safe=False)


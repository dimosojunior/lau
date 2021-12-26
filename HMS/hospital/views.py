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
import calendar
from calendar import HTMLCalendar


# Create your views here.


def search_tribe(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(tribe_choices__contains=query_original)
        #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryseti = Tribe.objects.filter(search)
    mylist= []
    mylist += [x.tribe  for x in queryseti]

    return JsonResponse(mylist, safe=False)

#CODES ZA KUPRINT DETAILS ZA WAGONJWA WENYE VIPIMO ZINAANZIA HAPA
def print_detail_watoto_vipimo(request, id):
    
    querySet = Vipimo.objects.get(id=id)
    template_path = 'hospital/print_detail.html'
    #querySet = KawaidaDozi.objects.get(id=id)
    context = {
        "querySet": querySet

    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    #if you want to download before opening it
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status= pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response

        
   
    #return render(request, 'hospital/print_detail.html',context)

def print_detail_kawaida_vipimo(request, id):
    
    querySet = KawaidaVipimo.objects.get(id=id)
    template_path = 'hospital/print_detail.html'
    #querySet = KawaidaDozi.objects.get(id=id)
    context = {
        "querySet": querySet

    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    #if you want to download before opening it
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status= pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response

        
   
    #return render(request, 'hospital/print_detail.html',context)
def print_detail_wazee_vipimo(request, id):
    
    querySet = WazeeVipimo.objects.get(id=id)
    template_path = 'hospital/print_detail.html'
    #querySet = KawaidaDozi.objects.get(id=id)
    context = {
        "querySet": querySet

    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    #if you want to download before opening it
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status= pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response

        
   
    #return render(request, 'hospital/print_detail.html',context)

def print_detail_wajawazito_vipimo(request, id):
    
    querySet = WajawazitoVipimo.objects.get(id=id)
    template_path = 'hospital/print_detail.html'
    #querySet = KawaidaDozi.objects.get(id=id)
    context = {
        "querySet": querySet

    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    #if you want to download before opening it
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status= pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response

        
   
    #return render(request, 'hospital/print_detail.html',context)

    #CODES ZA KUPRINT DETAILS ZA WAGONJWA WENYE VIPIMO ZINAISHIA HAPA



#CODES ZA KUPRINT DETAILS ZA WAGONJWA WENYE DOZI ZINAANZIA HAPA
def print_detail_watoto(request, id):
    
    querySet = Dozi.objects.get(id=id)
    template_path = 'hospital/print_detail.html'
    #querySet = KawaidaDozi.objects.get(id=id)
    context = {
        "querySet": querySet

    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    #if you want to download before opening it
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status= pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response

        
   
    #return render(request, 'hospital/print_detail.html',context)
def print_detail_kawaida(request, id):
    querySet = KawaidaDozi.objects.get(id=id)
    template_path = 'hospital/print_detail.html'
    #querySet = KawaidaDozi.objects.get(id=id)
    context = {
        "querySet": querySet

    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    #if you want to download before opening it
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status= pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response

        
   
    #return render(request, 'hospital/print_detail.html',context)

def print_detail_wazee(request, id):
    querySet = WazeeDozi.objects.get(id=id)
    template_path = 'hospital/print_detail.html'
    #querySet = KawaidaDozi.objects.get(id=id)
    context = {
        "querySet": querySet

    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    #if you want to download before opening it
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status= pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response

        
   
    #return render(request, 'hospital/print_detail.html',context)

def print_detail_wajawazito(request, id):
    querySet = WajawazitoDozi.objects.get(id=id)
    template_path = 'hospital/print_detail.html'
    #querySet = KawaidaDozi.objects.get(id=id)
    context = {
        "querySet": querySet

    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    #if you want to download before opening it
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status= pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response

        

    #return render(request, 'hospital/print_detail.html',context)


    #HIZO CODES ZINAISHIA HAPA
  
    

class base(TemplateView):
    template_name = 'hospital/base.html'
   
 

def daily_amount(request):

    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        enddate = request.POST.get('enddate')

        result = KawaidaDozi.objects.raw('select id, name, time_stamp, total from KAWAIDA_DOZI where time_stamp between "'+fromdate+'" and "'+enddate+'" ')
        context = {
        
        "queryset":result,
        }
        
    
        return render(request, 'hospital/daily_amount.html', context)
    else:

        start_date = datetime.date(2021,10,13)
        end_date = datetime.date(2021,12,30)

        myDate = datetime.datetime.now()
        myDate1 = datetime.datetime.now().date()
        myDate2 = datetime.datetime.now().time()
       # formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
       #from django.utils import timezone

      #now = timezone.now()
        
        queryset = KawaidaDozi.objects.filter(time_stamp__range=(start_date, end_date))
        
        
        context = {
            
            "queryset":queryset,
            "myDate": myDate,
            "myDate1": myDate1,
            "myDate2": myDate2
            
        }
       

        return render(request, 'hospital/daily_amount.html', context)



def uchafu(request, year=datetime.datetime.now().year,month=datetime.datetime.now().strftime('%B')):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        enddate = request.POST.get('enddate')

        result = KawaidaDozi.objects.raw('select id, name, time_stamp, total from KAWAIDA_DOZI where time_stamp between "'+fromdate+'" and "'+enddate+'" ')
        context = {
        
        "queryset":result,
        }
        
    
        return render(request, 'hospital/daily_amount.html', context)
    else:
        name = "john"
        month = month.capitalize()

        month_number = list(calendar.month_name).index(month)
        month_number = int(month_number)

        cal = HTMLCalendar().formatmonth(
            year,
            month_number


            )
        now = datetime.datetime.now()
        current_year = now.year

        event_list = KawaidaDozi.objects.filter(
            time_stamp__year = year,
            time_stamp__month = month_number

            )

        time = now.strftime('%I:%M %p')

        

            
        context = {
            
            
            "event_list": event_list,
            "name": name,
            "year": year,
            "month": month,
            "month_number": month_number,
            "cal": cal,
            "current_year": current_year,
            "time": time,
            
        }
           

        return render(request, 'hospital/uchafu.html', context)

   

    







def home(response):
    morning_workers_shift = MorningWorkersShift.objects.all()
    afternoon_workers_shift = AfternoonWorkersShift.objects.all()
    context = {
        "morning_workers_shift":morning_workers_shift,
        "afternoon_workers_shift":afternoon_workers_shift
    }
    
    return render(response, 'hospital/home.html',context)

def services(response):
    
    return render(response, 'hospital/services.html')

def list_of_dozi_vipimo(response):
    
    return render(response, 'hospital/list_of_dozi_vipimo.html')

def patients(response):
    
    return render(response, 'hospital/patients.html')



def doctors(response):
    doct = Doctors.objects.all()
    context = {
        "doct":doct
        
    }
    
    return render(response, 'hospital/doctors.html',context)



    
class watoto(SuccessMessageMixin, CreateView):
    model = WatotoService
    template_name = 'hospital/watoto.html'
    form_class = WatotoForm
    success_url = reverse_lazy('watoto_list')
    success_message = "Data Added Successfully"
    

class watoto_list(ListView):
    model = WatotoService
    template_name = 'hospital/watoto_list.html'
    context_object_name = 'watoto'
    paginate_by = 100

    def post(self, request):
        date = request.POST.get("date")

        appointment_id = request.POST.get("appointment-id")
        appointment = WatotoService.objects.get(id=appointment_id)
        appointment.accepted =True
        appointment.accepted_date = datetime.datetime.now()
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

    def get_queryset(self):
        return WatotoService.objects.order_by('-id')


class update_watoto(SuccessMessageMixin, UpdateView):
    model = WatotoService
    template_name = 'hospital/watoto.html'
    form_class = WatotoForm
    success_url = reverse_lazy('watoto_list')
    success_message = "Data Updated Successfully"

def delete_watoto(request, pk):
    watoto = get_object_or_404(WatotoService, id=pk)
    watoto.delete()
    return redirect('watoto_list')

#HIZI VIEWS KWA AJILI YA DOZI ZA WATOTO ZINAANZIA HAPA
#KWA AJILI YA KUADD DOZI ZA WATOTO
def add_dozi(request):
    
    form = DoziForm(request.POST or None)
    total_dozi = Dozi.objects.count()
    queryset = Dozi.objects.order_by('-id')[:3]  #hii ni kwa recent dozi
    if form.is_valid():
        form.save()
        return redirect('list_dozi')
    context = {
        "form":form,
        "title":"New Dozi",
        "total_dozi":total_dozi,
        "queryset":queryset
    }
    return render(request, 'hospital/add_dozi.html', context)
#KWA AJILIYA KUDISPLAY DOZI ZA WATOTO
def list_dozi(request):
    title = 'List of Dozi'
    queryset = Dozi.objects.filter(paid=False).order_by('-id')
    form = DoziSearchForm(request.POST or None)# form ya kuserch ila nimeifuta nimetumia hzo code za chini

    context = {
        "title":title,
        "queryset":queryset,
        "form":form
    }
    #searching button codes
    if request.method == 'POST':
        queryset = Dozi.objects.filter( name__icontains=form['name'].value())

    context = {
        "form":form,
        "title":title,
        "queryset":queryset
    }

    return render(request, 'hospital/list_dozi.html', context)
#KWA AJILI YA KUAPDATE DOZI ZA WATOTO
def dozi_update(request, pk):
    queryset = Dozi.objects.order_by('-id')[:2]

    querySet = Dozi.objects.get(id=pk)
    form = DoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = DoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            return redirect('/list_dozi')
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/add_dozi.html', context)

#HII NI KWA AJILI YA KUADD QUANTITY KWA WATOTO KWENYE SINGLE DETAIL LIST .HTML
def add_quantity(request, id):
    queryset = Dozi.objects.order_by('-id')[:2]

    querySet = Dozi.objects.get(id=id)
    form = DoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = DoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ADDED SUCCESSFULLY")
            return redirect('add_quantity',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_list_detail.html', context)

#HII NI KWA AJILI YA KUACCEPT MEDICINE KWA WATOTO KWENYE SINGLE DETAIL LIST .HTML
def accept_medicine(request, id):
    queryset = Dozi.objects.order_by('-id')[:2]

    querySet = Dozi.objects.get(id=id)
    form = DoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = DoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ALL MEDICINES ARE ACCEPTED SUCCESSFULLY")
            return redirect('accept_medicine',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_list_detail.html', context)

       

        
        
    
    
    


#HII NI KWA AJILI YA KUDELETE DOZI YAMTOTO KWENYE LIST DOZI.HTML
  
def dozi_delete(request, pk):
    watoto = get_object_or_404(Dozi, id=pk)
    watoto.delete()
    return redirect('list_dozi')

'''
def dozi_delete(request, pk):
    querySet = Dozi.objects.get(id=pk)
    
    if request.method == "POST":
        querySet.delete()
        
        return redirect('/list_dozi')
    
    
    return render(request, 'hospital/delete_dozi.html')
'''

'''
    
    





class C(SuccessMessageMixin, DeleteView):
    model = WatotoService
    template_name = 'hospital/delete_watoto.html'
    
    success_url = reverse_lazy('watoto_list')
    success_message = "Data Deleted Successfully"


'''
#hii ya chin ni kwaajili ya kumsearch mtu kwenye dozi_list.htm----->
def search_kipimo(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(name__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryset = Dozi.objects.filter(search)
    mylist= []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)


#hii ya chin ni kwaajili ya kumsearch mtoto kwenye add_dozi.htm----->
def search_mtoto(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(fname__contains=query_original)|Q(sname__contains=query_original)|Q(tname__contains=query_original)|Q(reg_no__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryseti = WatotoService.objects.filter(search)
    mylist= []
    mylist += [x.fname + '   ' + x.sname + '   ' + x.tname for x in queryseti]

    return JsonResponse(mylist, safe=False)


#VIEWS KWA AJILI YA DOZI ZINZISHIA HAPA








#HIZI ZA CHININI VIEWS KWAAJILI YA VIPIMO KWA WATOTO TU ZINAANZIA HAPA
#KWA  AJILL YA KUADD VIPIMO VYA WATOTO
def add_kipimo(request):
    
    form = VipimoForm(request.POST or None)
    total_dozi = Vipimo.objects.count()
    kipimo = Vipimo.objects.order_by('-id')[:3]  #hii ni kwa recent dozi
    if form.is_valid():
        form.save()
        return redirect('list_kipimo')
    context = {
        "form":form,
        "title":"New Dozi",
        "total_dozi":total_dozi,
        "kipimo":kipimo
    }
    return render(request, 'hospital/add_kipimo.html', context)

#KWA AJILI YA KUDISPLAY VIPIMO VYA WATOTO KWENYE LIST VIPIMO.HTML
def list_kipimo(request):
    title = 'List of Vipimo'
    kipimo = Vipimo.objects.filter(paid=False).order_by('-id')
    form = DoziSearchForm(request.POST or None)# form ya kuserch ila nimeifuta nimetumia hzo code za chini

    context = {
        "title":title,
        "kipimo":kipimo,
        "form":form
    }
    #searching button codes
    if request.method == 'POST':
        kipimo = Vipimo.objects.filter( name__icontains=form['name'].value())

    context = {
        "form":form,
        "title":title,
        "kipimo":kipimo
    }

    return render(request, 'hospital/list_vipimo.html', context)

#KWA AJILI YA KUAPDATE KIPIMO CHA MTOTO KWENYE LIST KIPIMO.HTML
def kipimo_update(request, pk):
    queryset = Vipimo.objects.order_by('-id')[:2]

    querySet = Vipimo.objects.get(id=pk)
    form = VipimoUpdateForm(instance=querySet)
    if request.method == "POST":
        form = VipimoUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            return redirect('/list_kipimo')
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/add_kipimo.html', context)

#KWA AJILI YA KUDELETE KIPIMO CHA MTOTO KWENYE LIST KIPIMO.HTML
def kipimo_delete(request, pk):
    watoto = get_object_or_404(Vipimo, id=pk)
    watoto.delete()
    return redirect('list_kipimo')

#HII NI YA KUACCEPT VIPIMO KWA AJILI YA WATOTO KWENYE SINGLE KIPIMO LIST.HTML
def accept_vipimo(request, id):
    queryset = Vipimo.objects.order_by('-id')[:2]

    querySet = Vipimo.objects.get(id=id)
    form = VipimoUpdateForm(instance=querySet)
    if request.method == "POST":
        form = VipimoUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ADDED SUCCESSFULLY")
            return redirect('accept_vipimo',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_kipimo_list.html', context)
#HIIYA ADD DAWA HAITUMIKI KWA SASA ILIKUWA NI YA WATOTO KWENYE SINGLE LIST DETAIL.HTML
def add_dawa(request, id):
    queryset = Vipimo.objects.order_by('-id')[:2]

    querySet = Vipimo.objects.get(id=id)
    form = VipimoUpdateForm(instance=querySet)
    if request.method == "POST":
        form = VipimoUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ALL MEDICINES ARE ACCEPTED SUCCESSFULLY")
            return redirect('add_dawa',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_kipimo_list.html', context)

#YA KUSERACH KIPIMO KWA WATOTO KWENYE LIST_VIPIMO.HTML
def search_kipimo2(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(name__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryset = Vipimo.objects.filter(search)
    mylist= []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)



#VIEWS KWA AJILI YA VIPIMO ZINAISHIA HAPA


#hVIEWS KWA AJILI YA WAZEE ZINAANZIA HAPA

class wazee(SuccessMessageMixin, CreateView):
    model = WazeeService
    template_name = 'hospital/wazee_add.html'
    form_class = WazeeForm
    success_url = reverse_lazy('wazee_list')
    success_message = "Elder Patient Added Successfully"

class wazee_list(ListView):
    model = WazeeService
    template_name = 'hospital/wazee_list.html'
    context_object_name = 'wazee'
    paginate_by = 100

    def post(self, request):
        date = request.POST.get("date")

        appointment_id = request.POST.get("appointment-id")
        appointment = WazeeService.objects.get(id=appointment_id)
        appointment.accepted =True
        appointment.accepted_date = datetime.datetime.now()
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

    def get_queryset(self):
        return WazeeService.objects.order_by('-id')


class update_wazee(SuccessMessageMixin, UpdateView):
    model = WazeeService
    template_name = 'hospital/wazee_add.html'
    form_class = WazeeForm
    success_url = reverse_lazy('wazee_list')
    success_message = "Elder Patient Updated Successfully"

def delete_wazee(request, pk):
    watoto = get_object_or_404(WazeeService, id=pk)
    watoto.delete()
    return redirect('wazee_list')

#VIEWS KWA AJILI YA WAZEE ZINAISHIA HAPA





#hVIEWS KWA AJILI YA WAJAWAZITO ZINAANZIA HAPA

class wajawazito(SuccessMessageMixin, CreateView):
    model = WajawazitoService
    template_name = 'hospital/wajawazito_add.html'
    form_class = WajawazitoForm
    success_url = reverse_lazy('wajawazito_list')
    success_message = "Pregnancy Mother Added Successfully"

class wajawazito_list(ListView):
    model = WajawazitoService
    template_name = 'hospital/wajawazito_list.html'
    context_object_name = 'wajawazito'
    paginate_by = 100

    def post(self, request):
        date = request.POST.get("date")

        appointment_id = request.POST.get("appointment-id")
        appointment = WajawazitoService.objects.get(id=appointment_id)
        appointment.accepted =True
        appointment.accepted_date = datetime.datetime.now()
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

    def get_queryset(self):
        return WajawazitoService.objects.order_by('-id')


class update_wajawazito(SuccessMessageMixin, UpdateView):
    model = WajawazitoService
    template_name = 'hospital/wajawazito_add.html'
    form_class = WajawazitoForm
    success_url = reverse_lazy('wajawazito_list')
    success_message = "Pregnancy Mother Updated Successfully"

def delete_wajawazito(request, pk):
    watoto = get_object_or_404(WajawazitoService, id=pk)
    watoto.delete()
    return redirect('wajawazito_list')

    #ZINAISHIA HAPA ZAWAJAWAZITO


#hVIEWS KWA AJILI YA WAGONJWA WA KAWAIDA ZINAANZIA HAPA

class kawaida(SuccessMessageMixin, CreateView):
    model = KawaidaService
    template_name = 'hospital/kawaida_add.html'
    form_class = KawaidaForm
    success_url = reverse_lazy('kawaida_list')
    success_message = "Patient Added Successfully"

class kawaida_list(ListView):
    model = KawaidaService
    template_name = 'hospital/kawaida_list.html'
    context_object_name = 'kawaida'
    paginate_by = 100

    def post(self, request):
        date = request.POST.get("date")

        appointment_id = request.POST.get("appointment-id")
        appointment = KawaidaService.objects.get(id=appointment_id)
        appointment.accepted =True
        appointment.accepted_date = datetime.datetime.now()
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

    def get_queryset(self):
        return KawaidaService.objects.order_by('-id')


class update_kawaida(SuccessMessageMixin, UpdateView):
    model = KawaidaService
    template_name = 'hospital/kawaida_add.html'
    form_class = KawaidaForm
    success_url = reverse_lazy('kawaida_list')
    success_message = "Patient Updated Successfully"

def delete_kawaida(request, pk):
    watoto = get_object_or_404(KawaidaService, id=pk)
    watoto.delete()
    return redirect('kawaida_list')

#hii ya chin ni kwaajili ya kumsearch mgonjwa wa kawaida kwenye add_dozi.htm----->
def search_kawaida(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(fname__contains=query_original)|Q(sname__contains=query_original)|Q(tname__contains=query_original)|Q(reg_no__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryseti = KawaidaService.objects.filter(search)
    mylist= []
    mylist += [x.fname + '   ' + x.sname + '   ' + x.tname for x in queryseti]

    return JsonResponse(mylist, safe=False)

def search_dozi_kawaida(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(name__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryset = KawaidaDozi.objects.filter(search)
    mylist= []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)

def search_kipimo_kawaida(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(name__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryset = KawaidaDozi.objects.filter(search)
    mylist= []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)


    #HIZI NIKWA AJILI YA WAGONJWA WA KAWAIDA KWA AJILI YA DOZI ZAO

def add_dozi_kawaida(request):
    
    form = KawaidaDoziForm(request.POST or None)
    total_dozi = KawaidaDozi.objects.count()
    queryset = KawaidaDozi.objects.order_by('-id')[:3]  #hii ni kwa recent dozi
    if form.is_valid():
        form.save()
        return redirect('list_dozi_kawaida')
    context = {
        "form":form,
        "title":"New Dozi",
        "total_dozi":total_dozi,
        "queryset":queryset
    }
    return render(request, 'hospital/add_dozi_kawaida.html', context)


def list_dozi_kawaida(request):
    title = 'List of Dozi'
    queryset = KawaidaDozi.objects.filter(paid=False).order_by('-id')
    form = DoziSearchForm(request.POST or None)# form ya kuserch ila nimeifuta nimetumia hzo code za chini

    context = {
        "title":title,
        "queryset":queryset,
        "form":form
    }
    #searching button codes
    if request.method == 'POST':
        queryset = KawaidaDozi.objects.filter( name__icontains=form['name'].value())

    context = {
        "form":form,
        "title":title,
        "queryset":queryset
    }

    return render(request, 'hospital/list_dozi_kawaida.html', context)

def dozi_update_kawaida(request, pk):
    queryset = KawaidaDozi.objects.order_by('-id')[:2]

    querySet = KawaidaDozi.objects.get(id=pk)
    form = KawaidaDoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = KawaidaDoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            return redirect('/list_dozi_kawaida')
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/add_dozi_kawaida.html', context)
def dozi_delete_kawaida(request, pk):
    watoto = get_object_or_404(KawaidaDozi, id=pk)
    watoto.delete()
    return redirect('list_dozi_kawaida')

#HIZI ZA CHININI VIEWS KWAAJILI YA VIPIMO KWA WAGONJWA WA KAWAIDA TU ZINAANZIA HAPA

def add_kipimo_kawaida(request):
    
    form = KawaidaVipimoForm(request.POST or None)
    total_dozi = KawaidaVipimo.objects.count()
    kipimo = KawaidaVipimo.objects.order_by('-id')[:3]  #hii ni kwa recent dozi
    if form.is_valid():
        form.save()
        return redirect('list_kipimo_kawaida')
    context = {
        "form":form,
        "title":"New Dozi",
        "total_dozi":total_dozi,
        "kipimo":kipimo
    }
    return render(request, 'hospital/add_kipimo_kawaida.html', context)


def list_kipimo_kawaida(request):
    title = 'List of Vipimo'
    kipimo = KawaidaVipimo.objects.filter(paid=False).order_by('-id')
    form = DoziSearchForm(request.POST or None)# form ya kuserch ila nimeifuta nimetumia hzo code za chini

    context = {
        "title":title,
        "kipimo":kipimo,
        "form":form
    }
    #searching button codes
    if request.method == 'POST':
        kipimo = KawaidaVipimo.objects.filter( name__icontains=form['name'].value())

    context = {
        "form":form,
        "title":title,
        "kipimo":kipimo
    }

    return render(request, 'hospital/list_kipimo_kawaida.html', context)


def kipimo_update_kawaida(request, pk):
    queryset = KawaidaVipimo.objects.order_by('-id')[:2]

    querySet = KawaidaVipimo.objects.get(id=pk)
    form = KawaidaVipimoUpdateForm(instance=querySet)
    if request.method == "POST":
        form = KawaidaVipimoUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            return redirect('/list_kipimo_kawaida')
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/add_kipimo.html', context)


def kipimo_delete_kawaida(request, pk):
    watoto = get_object_or_404(KawaidaVipimo, id=pk)
    watoto.delete()
    return redirect('list_kipimo_kawaida')

def add_quantity_kawaida(request, id):
    queryset = KawaidaDozi.objects.order_by('-id')[:2]

    querySet = KawaidaDozi.objects.get(id=id)
    form = KawaidaDoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = KawaidaDoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ADDED SUCCESSFULLY")
            return redirect('add_quantity_kawaida',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_list_detail_dozi_kawaida.html', context)

def accept_medicine_kawaida(request, id):
    queryset = KawaidaDozi.objects.order_by('-id')[:2]

    querySet = KawaidaDozi.objects.get(id=id)
    form = KawaidaDoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = KawaidaDoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ALL MEDICINES ARE ACCEPTED SUCCESSFULLY")
            return redirect('accept_medicine_kawaida',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_list_detail_dozi_kawaida.html', context)



def accept_vipimo_kawaida(request, id):
    queryset = KawaidaVipimo.objects.order_by('-id')[:2]

    querySet = KawaidaVipimo.objects.get(id=id)
    form = KawaidaVipimoUpdateForm(instance=querySet)
    if request.method == "POST":
        form = KawaidaVipimoUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ADDED SUCCESSFULLY")
            return redirect('accept_vipimo_kawaida',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_list_detail_kipimo_kawaida.html', context)

    #MWISHO WA VIEWS KWA WAGONJWA WA KAWAIDA



    #VIEWS KWA AJILI YA KUADD WAZEE ZINAANZIA HAPA
def add_dozi_wazee(request):
    
    form = WazeeDoziForm(request.POST or None)
    total_dozi = WazeeDozi.objects.count()
    queryset = WazeeDozi.objects.order_by('-id')[:3]  #hii ni kwa recent dozi
    if form.is_valid():
        form.save()
        return redirect('list_dozi_wazee')
    context = {
        "form":form,
        "title":"New Dozi",
        "total_dozi":total_dozi,
        "queryset":queryset
    }
    return render(request, 'hospital/add_dozi_wazee.html', context)


def list_dozi_wazee(request):
    title = 'List of Dozi'
    queryset = WazeeDozi.objects.filter(paid=False).order_by('-id')
    form = DoziSearchForm(request.POST or None)# form ya kuserch ila nimeifuta nimetumia hzo code za chini

    context = {
        "title":title,
        "queryset":queryset,
        "form":form
    }
    #searching button codes
    if request.method == 'POST':
        queryset = WazeeDozi.objects.filter( name__icontains=form['name'].value())

    context = {
        "form":form,
        "title":title,
        "queryset":queryset
    }

    return render(request, 'hospital/list_dozi_wazee.html', context)

def search_wazee(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(fname__contains=query_original)|Q(sname__contains=query_original)|Q(tname__contains=query_original)|Q(reg_no__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryseti = WazeeService.objects.filter(search)
    mylist= []
    mylist += [x.fname + '   ' + x.sname + '   ' + x.tname for x in queryseti]

    return JsonResponse(mylist, safe=False)

def search_dozi_wazee(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(name__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryset = WazeeDozi.objects.filter(search)
    mylist= []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)

def search_kipimo_wazee(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(name__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryset = WazeeVipimo.objects.filter(search)
    mylist= []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)

def dozi_update_wazee(request, pk):
    queryset = WazeeDozi.objects.order_by('-id')[:2]

    querySet = WazeeDozi.objects.get(id=pk)
    form = WazeeDoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = WazeeDoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            return redirect('/list_dozi_wazee')
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/add_dozi_wazee.html', context)
def dozi_delete_wazee(request, pk):
    watoto = get_object_or_404(WazeeDozi, id=pk)
    watoto.delete()
    return redirect('list_dozi_wazee')


#HIZI ZA CHININI VIEWS KWAAJILI YA VIPIMO KWA WAZEE TU ZINAANZIA HAPA

def add_kipimo_wazee(request):
    
    form = WazeeVipimoForm(request.POST or None)
    total_dozi = WazeeVipimo.objects.count()
    kipimo = WazeeVipimo.objects.order_by('-id')[:3]  #hii ni kwa recent dozi
    if form.is_valid():
        form.save()
        return redirect('list_kipimo_wazee')
    context = {
        "form":form,
        "title":"New Dozi",
        "total_dozi":total_dozi,
        "kipimo":kipimo
    }
    return render(request, 'hospital/add_kipimo_wazee.html', context)


def list_kipimo_wazee(request):
    title = 'List of Vipimo'
    kipimo = WazeeVipimo.objects.filter(paid=False).order_by('-id')
    form = DoziSearchForm(request.POST or None)# form ya kuserch ila nimeifuta nimetumia hzo code za chini

    context = {
        "title":title,
        "kipimo":kipimo,
        "form":form
    }
    #searching button codes
    if request.method == 'POST':
        kipimo = WazeeVipimo.objects.filter( name__icontains=form['name'].value())

    context = {
        "form":form,
        "title":title,
        "kipimo":kipimo
    }

    return render(request, 'hospital/list_kipimo_wazee.html', context)


def kipimo_update_wazee(request, pk):
    queryset = WazeeVipimo.objects.order_by('-id')[:2]

    querySet = WazeeVipimo.objects.get(id=pk)
    form = WazeeVipimoUpdateForm(instance=querySet)
    if request.method == "POST":
        form = WazeeVipimoUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            return redirect('/list_kipimo_wazee')
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/add_kipimo_wazee.html', context)


def kipimo_delete_wazee(request, pk):
    watoto = get_object_or_404(WazeeVipimo, id=pk)
    watoto.delete()
    return redirect('list_kipimo_wazee')

def add_quantity_wazee(request, id):
    queryset = WazeeDozi.objects.order_by('-id')[:2]

    querySet = WazeeDozi.objects.get(id=id)
    form = WazeeDoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = WazeeDoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ADDED SUCCESSFULLY")
            return redirect('add_quantity_wazee',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_list_detail_dozi_wazee.html', context)

def accept_medicine_wazee(request, id):
    queryset = WazeeDozi.objects.order_by('-id')[:2]

    querySet = WazeeDozi.objects.get(id=id)
    form = WazeeDoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = WazeeDoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ALL MEDICINES ARE ACCEPTED SUCCESSFULLY")
            return redirect('accept_medicine_wazee',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_list_detail_dozi_wazee.html', context)



def accept_vipimo_wazee(request, id):
    queryset = WazeeVipimo.objects.order_by('-id')[:2]

    querySet = WazeeVipimo.objects.get(id=id)
    form = WazeeVipimoUpdateForm(instance=querySet)
    if request.method == "POST":
        form = WazeeVipimoUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ADDED SUCCESSFULLY")
            return redirect('accept_vipimo_wazee',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_list_detail_kipimo_wazee.html', context)

#VIEWS ZA WAZEE ZINAISHIA HAPA


#HIZI ZA CHINI VIEWS KWA AJILI YA WAMAMA WAJAWAZITO ZINANZIA HAPA
  
def add_dozi_wajawazito(request):
    
    form = WajawazitoDoziForm(request.POST or None)
    total_dozi = WajawazitoDozi.objects.count()
    queryset = WajawazitoDozi.objects.order_by('-id')[:3]  #hii ni kwa recent dozi
    if form.is_valid():
        form.save()
        return redirect('list_dozi_wajawazito')
    context = {
        "form":form,
        "title":"New Dozi",
        "total_dozi":total_dozi,
        "queryset":queryset
    }
    return render(request, 'hospital/add_dozi_wajawazito.html', context)


def list_dozi_wajawazito(request):
    title = 'List of Dozi'
    queryset = WajawazitoDozi.objects.filter(paid=False).order_by('-id')
    form = DoziSearchForm(request.POST or None)# form ya kuserch ila nimeifuta nimetumia hzo code za chini

    context = {
        "title":title,
        "queryset":queryset,
        "form":form
    }
    #searching button codes
    if request.method == 'POST':
        queryset = WajawazitoDozi.objects.filter( name__icontains=form['name'].value())

    context = {
        "form":form,
        "title":title,
        "queryset":queryset
    }

    return render(request, 'hospital/list_dozi_wajawazito.html', context)

def search_wajawazito(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(fname__contains=query_original)|Q(sname__contains=query_original)|Q(tname__contains=query_original)|Q(reg_no__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryseti = WajawazitoService.objects.filter(search)
    mylist= []
    mylist += [x.fname + '   ' + x.sname + '   ' + x.tname for x in queryseti]

    return JsonResponse(mylist, safe=False)

def search_dozi_wajawazito(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(name__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryset = WajawazitoDozi.objects.filter(search)
    mylist= []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)

def search_kipimo_wajawazito(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(name__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryset = WajawazitoVipimo.objects.filter(search)
    mylist= []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)

def dozi_update_wajawazito(request, pk):
    queryset = WajawazitoDozi.objects.order_by('-id')[:2]

    querySet = WajawazitoDozi.objects.get(id=pk)
    form = WajawazitoDoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = WajawazitoDoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            return redirect('/list_dozi_wajawazito')
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/add_dozi_wajawazito.html', context)
def dozi_delete_wajawazito(request, pk):
    watoto = get_object_or_404(WajawazitoDozi, id=pk)
    watoto.delete()
    return redirect('list_dozi_wajawazito')

#HIZI ZA CHININI VIEWS KWAAJILI YA VIPIMO KWA WAZEE TU ZINAANZIA HAPA

def add_kipimo_wajawazito(request):
    
    form = WajawazitoVipimoForm(request.POST or None)
    total_dozi = WajawazitoVipimo.objects.count()
    kipimo = WajawazitoVipimo.objects.order_by('-id')[:3]  #hii ni kwa recent dozi
    if form.is_valid():
        form.save()
        return redirect('list_kipimo_wajawazito')
    context = {
        "form":form,
        "title":"New Dozi",
        "total_dozi":total_dozi,
        "kipimo":kipimo
    }
    return render(request, 'hospital/add_kipimo_wajawazito.html', context)


def list_kipimo_wajawazito(request):
    title = 'List of Vipimo'
    kipimo = WajawazitoVipimo.objects.filter(paid=False).order_by('-id')
    form = DoziSearchForm(request.POST or None)# form ya kuserch ila nimeifuta nimetumia hzo code za chini

    context = {
        "title":title,
        "kipimo":kipimo,
        "form":form
    }
    #searching button codes
    if request.method == 'POST':
        kipimo = WajawazitoVipimo.objects.filter( name__icontains=form['name'].value())

    context = {
        "form":form,
        "title":title,
        "kipimo":kipimo
    }

    return render(request, 'hospital/list_kipimo_wajawazito.html', context)


def kipimo_update_wajawazito(request, pk):
    queryset = WajawazitoVipimo.objects.order_by('-id')[:2]

    querySet = WajawazitoVipimo.objects.get(id=pk)
    form = WajawazitoVipimoUpdateForm(instance=querySet)
    if request.method == "POST":
        form = WajawazitoVipimoUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            return redirect('/list_kipimo_wajawazito')
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/add_kipimo_wajawazito.html', context)


def kipimo_delete_wajawazito(request, pk):
    watoto = get_object_or_404(WajawazitoVipimo, id=pk)
    watoto.delete()
    return redirect('list_kipimo_wajawazito')


def add_quantity_wajawazito(request, id):
    queryset = WajawazitoDozi.objects.order_by('-id')[:2]

    querySet = WajawazitoDozi.objects.get(id=id)
    form = WajawazitoDoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = WajawazitoDoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ADDED SUCCESSFULLY")
            return redirect('add_quantity_wajawazito',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_list_detail_dozi_wajawazito.html', context)

def accept_medicine_wajawazito(request, id):
    queryset = WajawazitoDozi.objects.order_by('-id')[:2]

    querySet = WajawazitoDozi.objects.get(id=id)
    form = WajawazitoDoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = WajawazitoDoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ALL MEDICINES ARE ACCEPTED SUCCESSFULLY")
            return redirect('accept_medicine_wajawazito',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_list_detail_dozi_wajawazito.html', context)



def accept_vipimo_wajawazito(request, id):
    queryset = WajawazitoVipimo.objects.order_by('-id')[:2]

    querySet = WajawazitoVipimo.objects.get(id=id)
    form = WajawazitoVipimoUpdateForm(instance=querySet)
    if request.method == "POST":
        form = WajawazitoVipimoUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ADDED SUCCESSFULLY")
            return redirect('accept_vipimo_wajawazito',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_list_detail_kipimo_wajawazito.html', context)









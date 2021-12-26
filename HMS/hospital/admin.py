#from hospital.forms import InvoiceForm
from django.contrib import admin
from hospital.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from hospital.forms import *


# Register your models here.
class MyUserAdmin(BaseUserAdmin):
    list_display=('first_name', 'middle_name', 'last_name', 'email', 'company_name', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_doctor', 'is_accountancy')
    search_fields=('email', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'first_name', 'middle_name', 'last_name', 'company_name', 'phone', 'password1', 'password2'),
        }),
    )

    ordering=('email',)



class DoziAdmin(admin.ModelAdmin):
    list_display=('name', 'total', 'time_stamp')
    form = DoziForm
    search_fields=('name',)
    
    
    list_filter=('name',)

class VipimoAdmin(admin.ModelAdmin):
    list_display=('name', 'total', 'time_stamp')
    form = VipimoForm
    search_fields=('name',)
    
    
    list_filter=('name',)


class WatotoAdmin(admin.ModelAdmin):
    list_display=('fname', 'sname', 'tname', 'reg_no')
    form = WatotoForm
    search_fields=('fname', 'sname', 'tname', 'reg_no')

class WazeeAdmin(admin.ModelAdmin):
    list_display=('fname', 'sname', 'tname', 'reg_no')
    form = WazeeForm
    search_fields=('fname', 'sname', 'tname', 'reg_no')

class WajawazitoAdmin(admin.ModelAdmin):
    list_display=('fname', 'sname', 'tname', 'reg_no')
    form = WajawazitoForm
    search_fields=('fname', 'sname', 'tname', 'reg_no')

class KawaidaAdmin(admin.ModelAdmin):
    list_display=('fname', 'sname', 'tname', 'reg_no')
    form = KawaidaForm
    search_fields=('fname', 'sname', 'tname', 'reg_no')

class KawaidaDoziAdmin(admin.ModelAdmin):
    list_display=('name', 'total', 'time_stamp')

    form = KawaidaDoziForm
    search_fields=('name',)
    
    
    list_filter=('name',)

class KawaidaVipimoAdmin(admin.ModelAdmin):
    list_display=('name', 'total', 'time_stamp')

    form = KawaidaVipimoForm
    search_fields=('name',)
    
    
    list_filter=('name',)

class WazeeVipimoAdmin(admin.ModelAdmin):
    list_display=('name', 'total', 'time_stamp')
    form = WazeeVipimoForm
    search_fields=('name',)
    
    
    list_filter=('name',)

class WazeeDoziAdmin(admin.ModelAdmin):
    list_display=('name', 'total', 'time_stamp')

    form = WazeeDoziForm
    search_fields=('name',)
    
    
    list_filter=('name',)

class WajawazitoVipimoAdmin(admin.ModelAdmin):
    list_display=('name', 'total', 'time_stamp')

    form = WajawazitoVipimoForm
    search_fields=('name',)
    
    
    list_filter=('name',)

class WajawazitoDoziAdmin(admin.ModelAdmin):
    list_display=('name', 'total', 'time_stamp')

    form = WajawazitoDoziForm
    search_fields=('name',)
    
    
    list_filter=('name',)

class AvailableMedicinesAdmin(admin.ModelAdmin):
    list_display=('medicine_name', 'quantity', 'price', 'created')
    form = AvailableMedicinesForm
    search_fields=('medicine_name',)
    
    
    list_filter=('medicine_name',)
    
    
    



admin.site.register(Doctors)
admin.site.register(Tribe)
admin.site.register(Appointment)

admin.site.register(MorningWorkersShift)
admin.site.register(AfternoonWorkersShift)
admin.site.register(WatotoService, WatotoAdmin)
admin.site.register(WazeeService, WazeeAdmin)
admin.site.register(WajawazitoService, WajawazitoAdmin)
admin.site.register(KawaidaService, KawaidaAdmin)
admin.site.register(Medicine)
admin.site.register(MyUser, MyUserAdmin)
#admin.site.register(Dozi)
admin.site.register(Dozi, DoziAdmin)
admin.site.register(Vipimo, VipimoAdmin)
admin.site.register(KawaidaDozi, KawaidaDoziAdmin)
admin.site.register(KawaidaVipimo, KawaidaVipimoAdmin)

admin.site.register(WazeeDozi, WazeeDoziAdmin)
admin.site.register(WazeeVipimo, WazeeVipimoAdmin)

admin.site.register(WajawazitoDozi, WajawazitoDoziAdmin)
admin.site.register(WajawazitoVipimo, WajawazitoVipimoAdmin)

admin.site.register(AvailableMedicines, AvailableMedicinesAdmin)



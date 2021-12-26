from django.urls import path
from .import views



urlpatterns = [

   
    path('', views.home, name="home"),
   
    path('base/', views.base.as_view(), name="base"),
    path('uchafu/', views.uchafu, name="uchafu"),
    path('daily_amount/', views.daily_amount, name="daily_amount"),
    path('search_tribe/', views.search_tribe, name="search_tribe"),
    path('print_detail_watoto/<int:id>/', views.print_detail_watoto, name="print_detail_watoto"),
    path('print_detail_kawaida/<int:id>/', views.print_detail_kawaida, name="print_detail_kawaida"),
    path('print_detail_wazee/<int:id>/', views.print_detail_wazee, name="print_detail_wazee"),
    path('print_detail_wajawazito/<int:id>/', views.print_detail_wajawazito, name="print_detail_wajawazito"),


    path('print_detail_watoto_vipimo/<int:id>/', views.print_detail_watoto_vipimo, name="print_detail_watoto_vipimo"),
    path('print_detail_wajawazito_vipimo/<int:id>/', views.print_detail_wajawazito_vipimo, name="print_detail_wajawazito_vipimo"),
    path('print_detail_kawaida_vipimo/<int:id>/', views.print_detail_kawaida_vipimo, name="print_detail_kawaida_vipimo"),
    path('print_detail_wazee_vipimo/<int:id>/', views.print_detail_wazee_vipimo, name="print_detail_wazee_vipimo"),









    path('services/', views.services, name="services"),
    path('patients/', views.patients, name="patients"),
    path('list_of_dozi_vipimo/', views.list_of_dozi_vipimo, name="list_of_dozi_vipimo"),
    path('doctors/', views.doctors, name="doctors"),
    path('watoto/', views.watoto.as_view(), name="watoto"),
    path('watoto_list/', views.watoto_list.as_view(), name="watoto_list"),
    path('update_watoto/<int:pk>/', views.update_watoto.as_view(), name="update_watoto"),
    path('delete_watoto/<int:pk>/', views.delete_watoto, name="delete_watoto"),
    #path('watoto_detail/<int:pk>/', views.watoto_detail.as_view(), name="watoto_detail"),


    #URL KWA AJILI YA DOZI ZINAANZIA HAPA
    path('add_dozi/', views.add_dozi, name="add_dozi"),
    path('list_dozi/', views.list_dozi, name="list_dozi"),
    path('dozi_update/<int:pk>/', views.dozi_update, name="dozi_update"),
    path('dozi_delete/<int:pk>/', views.dozi_delete, name="dozi_delete"),
    
    path('search_kipimo/', views.search_kipimo, name="search_kipimo"),
    path('search_mtoto/', views.search_mtoto, name="search_mtoto"),
    
    
    #path('dozi_update_quantity/<int:pk>/', views.dozi_update_quantity, name="dozi_update_quantity"),
    path('add_quantity/<int:id>/', views.add_quantity, name="add_quantity"),
    path('accept_medicine/<int:id>/', views.accept_medicine, name="accept_medicine"),
     #URL KWA AJILI YA DOZI ZINZISHIA HAPA



    
#HIZI URL NI KWA AJILI YA VIPIMO ZINAANZIA HAPA
    path('add_kipimo/', views.add_kipimo, name="add_kipimo"),
    path('list_kipimo/', views.list_kipimo, name="list_kipimo"),
    path('kipimo_update/<int:pk>/', views.kipimo_update, name="kipimo_update"),
    path('kipimo_delete/<int:pk>/', views.kipimo_delete, name="kipimo_delete"),
    path('add_dawa/<int:id>/', views.add_dawa, name="add_dawa"),
    path('accept_vipimo/<int:id>/', views.accept_vipimo, name="accept_vipimo"),
    path('search_kipimo2/', views.search_kipimo2, name="search_kipimo2"),

 #URL KWA AJILI YA VIPIMO ZINZISHIA HAPA

   #hizi ni url kwa ajili ya wazee
     path('wazee/', views.wazee.as_view(), name="wazee"),
     path('wazee_list/', views.wazee_list.as_view(), name="wazee_list"),
     path('update_wazee/<int:pk>/', views.update_wazee.as_view(), name="update_wazee"),
     path('delete_wazee/<int:pk>/', views.delete_wazee, name="delete_wazee"),


     #HIZI NI URLS KWA AJILI YA WAJAWAZITO
     path('wajawazito/', views.wajawazito.as_view(), name="wajawazito"),
     path('wajawazito_list/', views.wajawazito_list.as_view(), name="wajawazito_list"),
     path('update_wajawazito/<int:pk>/', views.update_wajawazito.as_view(), name="update_wajawazito"),
     path('delete_wajawazito/<int:pk>/', views.delete_wajawazito, name="delete_wajawazito"),


     #HIZI NI URLS KWA AJILI YA WAgomjwa wa kawaida
     path('kawaida/', views.kawaida.as_view(), name="kawaida"),
     path('kawaida_list/', views.kawaida_list.as_view(), name="kawaida_list"),
     path('update_kawaida/<int:pk>/', views.update_kawaida.as_view(), name="update_kawaida"),
     path('delete_kawaida/<int:pk>/', views.delete_kawaida, name="delete_kawaida"),
     path('search_kawaida/', views.search_kawaida, name="search_kawaida"),
     path('add_dozi_kawaida/', views.add_dozi_kawaida, name="add_dozi_kawaida"),
     path('list_dozi_kawaida/', views.list_dozi_kawaida, name="list_dozi_kawaida"),
     path('search_dozi_kawaida/', views.search_dozi_kawaida, name="search_dozi_kawaida"),
     path('dozi_update_kawaida/<int:pk>/', views.dozi_update_kawaida, name="dozi_update_kawaida"),
     path('dozi_delete_kawaida/<int:pk>/', views.dozi_delete_kawaida, name="dozi_delete_kawaida"),
     path('add_kipimo_kawaida/', views.add_kipimo_kawaida, name="add_kipimo_kawaida"),
     path('list_kipimo_kawaida/', views.list_kipimo_kawaida, name="list_kipimo_kawaida"),
     
     path('kipimo_update_kawaida/<int:pk>/', views.kipimo_update_kawaida, name="kipimo_update_kawaida"),
     path('kipimo_delete_kawaida/<int:pk>/', views.kipimo_delete_kawaida, name="kipimo_delete_kawaida"),
     path('search_kipimo_kawaida/', views.search_kipimo_kawaida, name="search_kipimo_kawaida"),
     path('add_quantity_kawaida/<int:id>/', views.add_quantity_kawaida, name="add_quantity_kawaida"),
     path('accept_medicine_kawaida/<int:id>/', views.accept_medicine_kawaida, name="accept_medicine_kawaida"),
     path('accept_vipimo_kawaida/<int:id>/', views.accept_vipimo_kawaida, name="accept_vipimo_kawaida"),

     #ZINAISHIA HAPA URLS KWA AJILIYA WAGONJWA WA KAWAIDA

     #HIZI URLS KWA AJILI YA WAZEE ZINAANZIA HAPA
     path('add_dozi_wazee/', views.add_dozi_wazee, name="add_dozi_wazee"),
     path('list_dozi_wazee/', views.list_dozi_wazee, name="list_dozi_wazee"),
     path('search_wazee/', views.search_wazee, name="search_wazee"),
     path('search_dozi_wazee/', views.search_dozi_wazee, name="search_dozi_wazee"),
     path('dozi_update_wazee/<int:pk>/', views.dozi_update_wazee, name="dozi_update_wazee"),
     path('dozi_delete_wazee/<int:pk>/', views.dozi_delete_wazee, name="dozi_delete_wazee"),
     path('add_kipimo_wazee/', views.add_kipimo_wazee, name="add_kipimo_wazee"),
     path('list_kipimo_wazee/', views.list_kipimo_wazee, name="list_kipimo_wazee"),
     
     path('kipimo_update_wazee/<int:pk>/', views.kipimo_update_wazee, name="kipimo_update_wazee"),
     path('kipimo_delete_wazee/<int:pk>/', views.kipimo_delete_wazee, name="kipimo_delete_wazee"),
     path('search_kipimo_wazee/', views.search_kipimo_wazee, name="search_kipimo_wazee"),

     path('add_quantity_wazee/<int:id>/', views.add_quantity_wazee, name="add_quantity_wazee"),
     path('accept_medicine_wazee/<int:id>/', views.accept_medicine_wazee, name="accept_medicine_wazee"),
     path('accept_vipimo_wazee/<int:id>/', views.accept_vipimo_wazee, name="accept_vipimo_wazee"),



     #HIZ NI URLS KWA AJILI YA WAJAWAZITO  TU ZINAANZIA HAPA
     path('add_dozi_wajawazito/', views.add_dozi_wajawazito, name="add_dozi_wajawazito"),
     path('list_dozi_wajawazito/', views.list_dozi_wajawazito, name="list_dozi_wajawazito"),
     path('search_wajawazito/', views.search_wajawazito, name="search_wajawazito"),
     path('search_dozi_wajawazito/', views.search_dozi_wajawazito, name="search_dozi_wajawazito"),
     path('dozi_update_wajawazito/<int:pk>/', views.dozi_update_wajawazito, name="dozi_update_wajawazito"),
     path('dozi_delete_wajawazito/<int:pk>/', views.dozi_delete_wajawazito, name="dozi_delete_wajawazito"),
     path('add_kipimo_wajawazito/', views.add_kipimo_wajawazito, name="add_kipimo_wajawazito"),
     path('list_kipimo_wajawazito/', views.list_kipimo_wajawazito, name="list_kipimo_wajawazito"),
     
     path('kipimo_update_wajawazito/<int:pk>/', views.kipimo_update_wajawazito, name="kipimo_update_wajawazito"),
     path('kipimo_delete_wajawazito/<int:pk>/', views.kipimo_delete_wajawazito, name="kipimo_delete_wajawazito"),
     path('search_kipimo_wajawazito/', views.search_kipimo_wajawazito, name="search_kipimo_wajawazito"),
     path('add_quantity_wajawazito/<int:id>/', views.add_quantity_wajawazito, name="add_quantity_wajawazito"),
     path('accept_medicine_wajawazito/<int:id>/', views.accept_medicine_wajawazito, name="accept_medicine_wajawazito"),
     path('accept_vipimo_wajawazito/<int:id>/', views.accept_vipimo_wajawazito, name="accept_vipimo_wajawazito"),


    
    
 
    
 
]
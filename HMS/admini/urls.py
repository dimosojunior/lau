from django.urls import path
from .import views



urlpatterns = [

   
    path('index', views.index, name="index"),

    #HIZI NI DOZIIIIII

    #HIZI NIKWA AJILI YA WATOTO
    path('list_watoto_dozi', views.list_watoto_dozi.as_view(), name="list_watoto_dozi"),
    path('update_watoto_dozi/<int:pk>/', views.update_watoto_dozi.as_view(), name="update_watoto_dozi"),
    
    path('delete_watoto_dozi/<int:pk>/', views.delete_watoto_dozi, name="delete_watoto_dozi"),
    path('watoto_dozi_view/<int:pk>/', views.watoto_dozi_view.as_view(), name="watoto_dozi_view"),

    #ZINAISHIA HAPA

    #HIZI NI KWA AJILI YA WAZEE
    path('list_wazee_dozi', views.list_wazee_dozi.as_view(), name="list_wazee_dozi"),
    path('update_wazee_dozi/<int:pk>/', views.update_wazee_dozi.as_view(), name="update_wazee_dozi"),
    
    path('delete_wazee_dozi/<int:pk>/', views.delete_wazee_dozi, name="delete_wazee_dozi"),
    path('wazee_dozi_view/<int:pk>/', views.wazee_dozi_view.as_view(), name="wazee_dozi_view"),


    #HIZI NI KWA AJILI YA WA kawaida
    path('list_kawaida_dozi', views.list_kawaida_dozi.as_view(), name="list_kawaida_dozi"),
    path('update_kawaida_dozi/<int:pk>/', views.update_kawaida_dozi.as_view(), name="update_kawaida_dozi"),
    
    path('delete_kawaida_dozi/<int:pk>/', views.delete_kawaida_dozi, name="delete_kawaida_dozi"),
    path('kawaida_dozi_view/<int:pk>/', views.kawaida_dozi_view.as_view(), name="kawaida_dozi_view"),


    #HIZI NI KWA AJILI YA WAjawazito
    path('list_wajawazito_dozi', views.list_wajawazito_dozi.as_view(), name="list_wajawazito_dozi"),
    path('update_wajawazito_dozi/<int:pk>/', views.update_wajawazito_dozi.as_view(), name="update_wajawazito_dozi"),
    
    path('delete_wajawazito_dozi/<int:pk>/', views.delete_wajawazito_dozi, name="delete_wajawazito_dozi"),
    path('wajawazito_dozi_view/<int:pk>/', views.wajawazito_dozi_view.as_view(), name="wajawazito_dozi_view"),



    #HIZI NI VIPIMOOOOO

    #KWA AJILI YA WATOTO

    path('list_watoto_vipimo', views.list_watoto_vipimo.as_view(), name="list_watoto_vipimo"),
    path('update_watoto_vipimo/<int:pk>/', views.update_watoto_vipimo.as_view(), name="update_watoto_vipimo"),
    
    path('delete_watoto_vipimo/<int:pk>/', views.delete_watoto_vipimo, name="delete_watoto_vipimo"),
    path('watoto_vipimo_view/<int:pk>/', views.watoto_vipimo_view.as_view(), name="watoto_vipimo_view"),
    #path('search_watoto_dozi/', views.search_watoto_dozi, name="search_watoto_dozi"),


    #HIZI NI KWA AJILI YA WAZEE
    path('list_wazee_vipimo', views.list_wazee_vipimo.as_view(), name="list_wazee_vipimo"),
    path('update_wazee_vipimo/<int:pk>/', views.update_wazee_vipimo.as_view(), name="update_wazee_vipimo"),
    
    path('delete_wazee_vipimo/<int:pk>/', views.delete_wazee_vipimo, name="delete_wazee_vipimo"),
    path('wazee_vipimo_view/<int:pk>/', views.wazee_vipimo_view.as_view(), name="wazee_vipimo_view"),


    #HIZI NI KWA AJILI YA WA kawaida
    path('list_kawaida_vipimo', views.list_kawaida_vipimo.as_view(), name="list_kawaida_vipimo"),
    path('update_kawaida_vipimo/<int:pk>/', views.update_kawaida_vipimo.as_view(), name="update_kawaida_vipimo"),
    
    path('delete_kawaida_vipimo/<int:pk>/', views.delete_kawaida_vipimo, name="delete_kawaida_vipimo"),
    path('kawaida_vipimo_view/<int:pk>/', views.kawaida_vipimo_view.as_view(), name="kawaida_vipimo_view"),


    #HIZI NI KWA AJILI YA WAjawazito
    path('list_wajawazito_vipimo', views.list_wajawazito_vipimo.as_view(), name="list_wajawazito_vipimo"),
    path('update_wajawazito_vipimo/<int:pk>/', views.update_wajawazito_vipimo.as_view(), name="update_wajawazito_vipimo"),
    
    path('delete_wajawazito_vipimo/<int:pk>/', views.delete_wajawazito_vipimo, name="delete_wajawazito_vipimo"),
    path('wajawazito_vipimo_view/<int:pk>/', views.wajawazito_vipimo_view.as_view(), name="wajawazito_vipimo_view"),


    #MWISHO WA YOTE NI HAPA

    path('all_time_payment/', views.all_time_payment, name="all_time_payment"),
    path('today_payment/', views.today_payment, name="today_payment"),
    path('available_medicines/', views.available_medicines, name="available_medicines"),
    path('add_available_medicines/', views.add_available_medicines.as_view(), name="add_available_medicines"),
    path('update_available_medicines/<int:pk>/', views.update_available_medicines.as_view(), name="update_available_medicines"),
    path('delete_available_medicines/<int:pk>/', views.delete_available_medicines, name="delete_available_medicines"),
    
    path('search_available_medicines/', views.search_available_medicines, name="search_available_medicines"),
 
]
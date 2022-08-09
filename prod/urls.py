from django.urls import path,include
from . import views
from . import approv
from . import production



urlpatterns = [
    path('',views.acceuil,name='acceuil'),
    path('Approvisionnement',approv.redirectionapprov,name='approvLien'), 
    path('Production',production.redirectionproduction,name='prodLien') ,  
]

from django.urls import path,include
from . import views
from . import approv

urlpatterns = [
    path('',views.acceuil,name='acceuil'),
    path('Approvisionnement',approv.redirectionapprov,name='approvLien')    
]

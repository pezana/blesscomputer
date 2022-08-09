from django.urls import path,include
from . import views
from . import approv
from . import production
from . import fournisseur
from . import fen_EtapeDeProduction
from . import fen_stockAVendre



urlpatterns = [
    path('',views.acceuil,name='acceuil'),
    path('Approvisionnement',approv.redirectionapprov,name='approvLien'), 
    path('Production',production.redirectionproduction,name='prodLien'),
    path('Fournisseur',fournisseur.redirectionfournisseur,name='fournisseurLien'),
    path('Etape', fen_EtapeDeProduction.redirectionEtape, name='EtapeLien'),
    path('stockVente', fen_stockAVendre.redirectionstockvente, name='stockeventeLien')

]

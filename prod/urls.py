from django.urls import path,include
from . import views
from . import approv
from . import production
from . import fournisseur
from . import fen_EtapeDeProduction
<<<<<<< HEAD
from . import client
=======
from . import fen_stockAVendre

>>>>>>> c8877faaf9af91db10295ce32c32603f55962444


urlpatterns = [
    path('',views.acceuil,name='acceuil'),
    path('Approvisionnement',approv.redirectionapprov,name='approvLien'), 
    path('Production',production.redirectionproduction,name='prodLien'),
    path('Fournisseur',fournisseur.redirectionfournisseur,name='fournisseurLien'),
    path('Etape', fen_EtapeDeProduction.redirectionEtape, name='EtapeLien'),
<<<<<<< HEAD
    path('client', client.redirectionclient, name='clientLien')
=======
    path('stockVente', fen_stockAVendre.redirectionstockvente, name='stockeventeLien')
>>>>>>> c8877faaf9af91db10295ce32c32603f55962444

]

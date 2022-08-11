from django.shortcuts import render
from prod.models import *
from django.shortcuts import get_object_or_404

# la fonction de redirection vers la page des appprovisionnements
# get_object_or_404 pour gerer les erreurs 
def redirectionapprov(request):
     listeapprov=approvisionnement.objects.all()
     return render(request,'approv.html',{'liste':listeapprov})

# la fonction de redirection vers la page des details des approvisionnements
def voirApprov(request, id):
     voir_APPROVI = get_object_or_404(approvisionnement, id = id)
     return render(request,'detailsapprov.html', {'mondetail': voir_APPROVI})     
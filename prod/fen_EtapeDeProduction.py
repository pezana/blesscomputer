from django.shortcuts import render
from prod.models import *
from django.shortcuts import get_object_or_404

def redirectionEtape(request):
     EtapeList = etape.objects.all()
     return render(request,'fen_EtapeDeProduction.html', {'listEtape':EtapeList})

def voirDetail(request, id):
     voir_ETape = get_object_or_404(etape, id = id)
     return render(request,'voirEtape.html', {'undetail':voir_ETape})
     
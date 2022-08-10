from django.shortcuts import render
from prod.models import *


def redirectionEtape(request):
     EtapeList = etape.objects.all()
     return render(request,'fen_EtapeDeProduction.html', {'listEtape':EtapeList})
from django.shortcuts import render
from prod.models import *


def redirectionapprov(request):
     listeapprov=approvisionnement.objects.all()
     return render(request,'approv.html',{'liste':listeapprov})
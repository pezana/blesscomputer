from django.shortcuts import render
from .models import *


def redirectionproduction(request):
     listeprod=production.objects.all()
     return render(request,'production.html',{'liste':listeprod})

def detailproduit(request, id):
     undetail= production.objects.get(id=id)
     return render(request,'detailsProduction.html',{'liste':undetail})
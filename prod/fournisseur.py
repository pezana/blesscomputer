from django.shortcuts import render
from prod.models import *


def redirectionfournisseur(request):
     return render(request,'fournisseur.html')
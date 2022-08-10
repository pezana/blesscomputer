from django.shortcuts import render
from prod.models import *


def redirectionfournisseur(request):
     FournisseurList = fournisseur.objects.all()
     return render(request,'fournisseur.html', {'listFournisseur':FournisseurList})
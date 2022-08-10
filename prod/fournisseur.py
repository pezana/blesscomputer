from django.shortcuts import render
from prod.models import *
from django.shortcuts import get_object_or_404



def redirectionfournisseur(request):
     FournisseurList = fournisseur.objects.all()
     return render(request,'fournisseur.html', {'listFournisseur':FournisseurList})

def voirfournisseur(request, id):
     voirfournisseur = get_object_or_404(fournisseur, id = id)
     return render(request,'voirFournisseur.html', {'detailfournisseur':voirfournisseur})
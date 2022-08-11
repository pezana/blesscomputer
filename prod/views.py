from django.shortcuts import render , redirect
from.formulaire import fournisseurForm

# Create your views here.
def acceuil(request):
    return render(request,'home.html')


from django.shortcuts import render
from .models import *
from django import forms
from django.shortcuts import get_object_or_404


def redirectionutilisateur(request):
     listeutilisateur=utilisateur.objects.all()
     return render(request,'utilisateur.html',{'liste':listeutilisateur})


def voirUtilisateur(request, id):
     voir_Utilisateur = get_object_or_404(utilisateur, id = id)
     return render(request,'detailUtilisateur.html', {'monutilisateur': voir_Utilisateur})     
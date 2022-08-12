from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django import forms

def redirectionutilisateur(request):
     listeutilisateur=utilisateur.objects.all()
     return render(request,'utilisateur.html',{'liste':listeutilisateur})


def voirUtilisateur(request, id):
     voir_Utilisateur = get_object_or_404(utilisateur, id = id)
     return render(request,'detailUtilisateur.html', {'monuser': voir_Utilisateur})   



class ajoututilisateurform(forms.Form):     
      profil=forms.CharField(label='nom utilisateur')
      pseudo=forms.CharField(required=True)
      mdepass=forms.CharField(required=True)
          
#  la fonction qui permet d'ajouter les utilisateurs dans la base de donnees    
def ajoututilisateur(request):
     form=ajoututilisateurform()
     if request.POST:
          form=ajoututilisateurform(request.POST)  
          if form.is_valid():  
               prod= utilisateur.objects.create(**form.cleaned_data)                            
               prod.save()  
               form=ajoututilisateurform() 
               return render(request,'ajouterutilisateur.html',{'form':form,'msg':'ajout utilisateur avec succès'}) 
          else :
               form=ajoututilisateurform() 
               return render(request,'ajouterutilisateur.html',{'form':form,'msg':'vos information sont invalides'})
     else :
          form=ajoututilisateurform()
          return render(request,'ajouterutilisateur.html',{'form':form})               

def utilisateurjouter(request):
     return render(request,'ajouterutilisateur.html')
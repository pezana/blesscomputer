from django.shortcuts import render 
from prod.models import *
from django.shortcuts import get_object_or_404
from django import forms




def redirectionfournisseur(request):
     FournisseurList = fournisseur.objects.all()
     return render(request,'fournisseur.html', {'listFournisseur':FournisseurList})

def voirfournisseur(request, id):
     voirfournisseur = get_object_or_404(fournisseur, id = id)
     return render(request,'voirFournisseur.html', {'detailfournisseur':voirfournisseur})

class ajoutfournisseurform(forms.Form):     
     nom=forms.CharField(label='nom utilisateur',required=True)
     adresse=forms.CharField()
     tel=forms.CharField()

def ajoutfournisseur(request):
     form=ajoutfournisseurform()
     if request.POST:
          form=ajoutfournisseurform(request.POST)  
          if form.is_valid():  
               prod= fournisseur.objects.create(**form.cleaned_data)                            
               prod.save()  
               form=ajoutfournisseurform() 
               return render(request,'ajouterfournisseur.html',{'form':form,'msg':'ajout de la production avec succès'}) 
          else :
               form=ajoutfournisseurform() 
               return render(request,'ajouterfournisseur.html',{'form':form,'msg':'vos information sont invalides'})
     else :
          form=ajoutfournisseurform()
          return render(request,'ajouterfournisseur.html',{'form':form})               

def fourajouter(request):
     return render(request,'ajouterfournisseur.html')
from django.shortcuts import render
from .models import *
from django import forms
from django.shortcuts import get_object_or_404


def redirectionEtape(request):
     EtapeList = etape.objects.all()
     return render(request,'fen_EtapeDeProduction.html', {'listEtape':EtapeList})

def voirDetail(request, id):
     voir_ETape = get_object_or_404(etape, id = id)
     return render(request,'voirEtape.html', {'undetail':voir_ETape})

class ajoutetape(forms.Form):
     libelle=forms.CharField(max_length=100)  
     qteproduite=forms.IntegerField()
     qtedechet=forms.IntegerField()
     prod=forms.CharField()
     coutdeletape=forms.DecimalField()
     description=forms.CharField()
     def __str__(self):
        return self.prod
     

def fonc_ajouter(request):
     formEtape=ajoutetape()
     if request.POST:
          formEtape=ajoutetape(request.POST)  
          if formEtape.is_valid():  
               etap= etape.objects.create(**formEtape.cleaned_data)                            
               etap.save()  
               formEtape=ajoutetape() 
               return render(request,'NewEtape.html',{'form':formEtape,'msg':'ajout de la production avec succès'}) 
          else :
               formEtape=ajoutetape() 
               return render(request,'NewEtape.html',{'form':formEtape,'msg':'vos information sont invalides'})
     else :
          formEtape=ajoutetape()
          return render(request,'NewEtape.html',{'form':formEtape})               
 

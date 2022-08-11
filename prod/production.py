from django.shortcuts import render
from .models import *
from django import forms


def redirectionproduction(request):
     listeprod=production.objects.all()
     return render(request,'production.html',{'liste':listeprod})

def detailproduit(request, id):
     undetail= production.objects.get(id=id)
     return render(request,'detailsProduction.html',{'liste':undetail})

class ajoutproductionform(forms.Form):     
     codeprod=forms.CharField(label='code de la production',required=True)
     qte=forms.IntegerField()
     dteprod=forms.DateField()
     qtedechet=forms.IntegerField()
    
          
     
def ajoutproduction(request):
     form=ajoutproductionform()
     if request.POST:
          form=ajoutproductionform(request.POST)  
          if form.is_valid():  
               prod= production.objects.create(**form.cleaned_data)                            
               prod.save()  
               form=ajoutproductionform() 
               return render(request,'ajouterproduction.html',{'form':form,'msg':'ajout de la production avec succès'}) 
          else :
               form=ajoutproductionform() 
               return render(request,'ajouterproduction.html',{'form':form,'msg':'vos information sont invalides'})
     else :
          form=ajoutproductionform()
          return render(request,'ajouterproduction.html',{'form':form})               

def redajouter(request):
     return render(request,'ajouterproduction.html')                     
                                           
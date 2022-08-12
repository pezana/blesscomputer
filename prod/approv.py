from django.shortcuts import render
from prod.models import *
from django import forms
from django.shortcuts import get_object_or_404

# la fonction de redirection vers la page des appprovisionnements
# get_object_or_404 pour gerer les erreurs 
def redirectionapprov(request):
     listeapprov=approvisionnement.objects.all()
     return render(request,'approv.html',{'liste':listeapprov})

# la fonction de redirection vers la page des details des approvisionnements
def voirApprov(request, id):
     voir_APPROVI = get_object_or_404(approvisionnement, id = id)
     return render(request,'detailsapprov.html', {'mondetail': voir_APPROVI})     


##
##
##
# formulaire approvisionnement
class ajoutapprovform(forms.Form):   
      dte=forms.DateField(label='date approvisionnement', required=True) 
      coutachat=forms.FloatField()
      coutsupp=forms.FloatField()      
      fournisseur=forms.ChoiceField()
          
     
def ajoutapprov(request):
     form=ajoutapprovform()
     if request.POST:
          form=ajoutapprovform(request.POST)  
          if form.is_valid():  
               approv= approvisionnement.objects.create(**form.cleaned_data)                            
               approv.save()  
               form=ajoutapprovform() 
               return render(request,'ajouterapprov.html',{'form':form,'msg':'ajout approvisionnement avec succès'}) 
          else :
               form=ajoutapprovform() 
               return render(request,'ajouterapprov.html',{'form':form,'msg':'vos information sont invalides'})
     else :
          form=ajoutapprovform()
          return render(request,'ajouterapprov.html',{'form':form})               

def approvajouter(request):
     return render(request,'ajouterapprov.html')                
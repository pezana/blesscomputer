from django.shortcuts import render
from prod.models import *
from django.shortcuts import get_object_or_404
from django import forms


def redirectionclient(request):
    listeclient=client.objects.all()
    return render(request,'client.html',{'liste':listeclient})

def detailclient(request, id):
    voir_client= get_object_or_404(client, id= id)
    return render(request,'detailclient.html',{'maliste': voir_client})

class ajoutclientform(forms.Form):
     nom=forms.CharField(label='',required=True, widget=forms.TextInput( 
          attrs={
               'PlaceHolder': 'nom du client', 

          }))
     adress=forms.CharField(label='',required=True, widget=forms.TextInput( 
          attrs={
               'PlaceHolder': 'adresse du client',

          }))
     tel=forms.CharField(label='',required=True, widget=forms.TextInput( 
          attrs={
               'PlaceHolder': 'telephone',     

          }))
     typeclient=forms.CharField(label='',required=True, widget=forms.TextInput( 
          attrs={
               'PlaceHolder': 'type de client',
          }))          

          
     
def ajoutclient(request):
     form=ajoutclientform()
     if request.POST:
          form=ajoutclientform(request.POST)  
          if form.is_valid():  
               prod= client.objects.create(**form.cleaned_data)                            
               prod.save()  
               form=ajoutclientform() 
               return render(request,'ajouterclient.html',{'form':form,'msg':'ajout du client avec succès'}) 
          else :
               form=ajoutclientform() 
               return render(request,'ajouterclient.html',{'form':form,'msg':'vos information sont invalides'})
     else :
          form=ajoutclientform()
          return render(request,'ajouterclient.html',{'form':form})               

def clientjouter(request):
     return render(request,'ajouterclient.html')
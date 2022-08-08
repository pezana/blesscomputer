from django.db import models

# Create your models here.
from email.policy import default
from django.db import models

# Create your models here.

class client(models.Model):
    nom=models.CharField(max_length=100)
    adress=models.CharField(max_length=100)
    tel=models.CharField(max_length=9)
    typeclient=models.CharField(max_length=100)
   

class production(models.Model):
    codeprod=models.CharField(max_length=100) 
    qte=models.IntegerField(default=0)
    dteprod=models.DateField(blank=True,null=True)
    qtedechet=models.IntegerField(default=0)

class etape(models.Model):
    libelle=models.CharField(max_length=100)  
    qteproduite=models.IntegerField()
    qtedechet=models.IntegerField()
    prod=models.ForeignKey(production,null=True,on_delete=models.CASCADE)
    coutdeletape=models.DecimalField(max_digits=10000,decimal_places=2)
    description=models.TextField()
    
class fournisseur(models.Model):
    nom=models.CharField(max_length=100)  
    adresse=models.CharField(max_length=100) 
    tel=models.CharField(max_length=10)
    
class approvisionnement(models.Model) :
    dte=models.DateField(blank=True, null=True) 
    coutachat=models.FloatField(blank=True)
    coutsupp=models.FloatField(blank=True) 
    fournisseur=models.ForeignKey(fournisseur,on_delete=models.CASCADE)

class stockapp(models.Model):
    qteapp=models.IntegerField(null=True) 
    qteappseuil=models.IntegerField(null=True,default=0)
       
class stockvente(models.Model):
    qtevente=models.IntegerField(default=0)    
    qtedechet=models.IntegerField(default=0)

class utilisateur(models.Model):
    profil=models.CharField(max_length=100)
    pseudo=models.CharField(max_length=50)
    mdepass=models.CharField(max_length=50)

class facture(models.Model):
    codevente=models.CharField(max_length=10)    
    dtevente=models.DateField(auto_now_add=True,)
    prix=models.FloatField(null=True,default=0)
    utilisateur=models.ForeignKey(utilisateur,on_delete=models.CASCADE)
    def generercode(self):
        nbreelt=facture.odjects.all()
        self.codevente="FACT"+(nbreelt+1)
        return self.codevente
        
class vente(models.Model):
    qte=models.IntegerField(default=0)
    prix=models.FloatField(default=0)
    facture=models.ForeignKey(facture,on_delete=models.CASCADE,null=True)
    client=models.ForeignKey(client,on_delete=models.CASCADE,null=True)    

     

    
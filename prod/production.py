from django.shortcuts import render
from .models import *


def redirectionproduction(request):
     listeprod=production.objects.all()
     return render(request,'production.html',{'liste':listeprod})
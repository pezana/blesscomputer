from django.shortcuts import render
from prod.models import *


def redirectionapprov(request):
     return render(request,'approv.html')
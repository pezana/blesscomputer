from django.shortcuts import render
from prod.models import *


def redirectionproduction(request):
     return render(request,'production.html')
from django.shortcuts import render
from prod.models import *


def redirectionclient(request):
     return render(request,'client.html')
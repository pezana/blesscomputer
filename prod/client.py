from django.shortcuts import render
from prod.models import *


def redirectionclient(request):
    listeclient=client.objects.all()
    return render(request,'client.html',{'liste':listeclient})
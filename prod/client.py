from django.shortcuts import render
from prod.models import *
from django.shortcuts import get_object_or_404


def redirectionclient(request):
    listeclient=client.objects.all()
    return render(request,'client.html',{'liste':listeclient})

def detailclient(request, id):
    voir_client= get_object_or_404(client, id= id)
    return render(request,'detailclient.html',{'maliste': voir_client})
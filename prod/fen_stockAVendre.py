from django.shortcuts import render
from prod.models import *


def redirectionstockvente(request):
     return render(request,'fen_stockAVendre.html')
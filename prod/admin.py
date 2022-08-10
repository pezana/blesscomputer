from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(client)
admin.site.register(fournisseur)
admin.site.register(approvisionnement)
admin.site.register(production)
admin.site.register(stockapp)
admin.site.register(stockvente)
admin.site.register(etape)






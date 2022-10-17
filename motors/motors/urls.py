from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from carros.views import *

router = routers.DefaultRouter()
router.register('revendedor', RevendedorViewSets, basename='revendedor')
router.register('marca', MarcaViewSets, basename='marca')
router.register('modelo', ModeloViewSets, basename='modelo')
router.register('carro', CarroViewSets, basename='carro')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
    
]
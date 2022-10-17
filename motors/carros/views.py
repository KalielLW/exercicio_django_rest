from rest_framework import viewsets

from motors.serializers import RevendedorSerializer, MarcaSerializer, ModeloSerializer, CarroSerializer

from carros.models import Revendedor, Marca, Modelo, Carro

class RevendedorViewSets(viewsets.ModelViewSet):
    queryset = Revendedor.objects.all()
    serializer_class = RevendedorSerializer
    http_method_names = ['get', 'post', 'delete']
    
class MarcaViewSets(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    http_method_names = ['get', 'post', 'delete']
    
class ModeloViewSets(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
    http_method_names = ['get', 'post', 'delete']
    
class CarroViewSets(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    http_method_names = ['get', 'post', 'delete']
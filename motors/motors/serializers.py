from rest_framework import serializers

from carros.models import Revendedor, Marca, Modelo, Carro

class RevendedorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Revendedor
        fields = ['id', 'nome', 'telefone', 'endereco']
        
class MarcaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Marca
        fields = ['id', 'nome', 'descricao']
        
class ModeloSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Modelo
        fields = ['id', 'nome', 'marca']
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['marca']= MarcaSerializer(instance.marca).data
        return response
        
class CarroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Carro
        fields = ['id', 'nome', 'valor', 'ano', 'modelo', 'revendedor']
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['revendedor'] = RevendedorSerializer(instance.revendedor).data
        response['modelo'] = ModeloSerializer(instance.modelo).data
        return response
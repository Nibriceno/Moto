from pyexpat import model
from .models import Vehiculo
from rest_framework import serializers

class vehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Vehiculo
        fields = 'patente' , 'marca' , 'modelo' ,'categoria'
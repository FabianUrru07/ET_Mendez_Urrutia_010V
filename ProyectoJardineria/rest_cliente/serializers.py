from rest_framework import serializers
from store.models import Cliente


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['rut','nombre','direccion','email','telefono']
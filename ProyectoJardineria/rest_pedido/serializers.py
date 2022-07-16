from rest_framework import serializers
from store.models import Pedido


class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['idPedido','idProducto','rut','estado']
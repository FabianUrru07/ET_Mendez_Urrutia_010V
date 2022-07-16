from django.urls import URLPattern, path
from .views import lista_pedidos


urlpatterns = [
    path('lista_pedidos', lista_pedidos, name="lista_pedidos"),
]
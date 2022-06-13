from django.urls import path,include
from .views import  salir,form_crear_producto, index, ver, cont, gale, somos, api, form_crear_producto,form_mod_producto,form_del_producto,mostrarProducto,form_crear_cliente,form_mod_cliente,form_del_cliente,mostrarCliente
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path ('ver/', ver, name="ver"),
    path ('cont/', cont, name="cont"),
    path ('gale/', gale, name="gale"),
    path ('somos/', somos, name="somos"),
    path ('api/', api, name="api"),
    path ('form_crear_producto/', form_crear_producto, name="form_crear_producto"),
    path ('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),
    path ('form_del_producto/<id>', form_del_producto, name="form_del_producto"),
    path ('mostrarProducto', mostrarProducto, name="mostrarProducto"),
    path ('form_crear_cliente/', form_crear_cliente, name="form_crear_cliente"),
    path ('form_mod_cliente/<id>', form_mod_cliente, name="form_mod_cliente"),
    path ('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),
    path ('mostrarCliente', mostrarCliente, name="mostrarCliente"),
    path ('accounts/login', include('django.contrib.auth.urls'),name="login"),
    path ('salir/',salir, name="logout")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
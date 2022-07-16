
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import  Producto, Cliente, Pedido



    

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        imagen  = forms.ImageField()
        imagen.widget.attrs.update({'class': 'form-control','id':'id_imagen'})
        fields = ['idProducto', 'nombre', 'precio','descripcion','imagen','stock']
        labels ={
            'IdProducto': 'Id', 
            'nombre': 'Nombre', 
            'precio': 'Precio', 
            'descripcion': 'Descripcion',
            'imagen' : 'Imagen',
            'stock' : 'Stock'
            
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Id', 
                    'id': 'idProducto'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese precio', 
                    'id': 'precio'
                }
            ), 
            'descripcion': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingrese Descripcion',
                    'id':'descripcion'
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingrese Stock',
                    'id':'stock'
                }
            ),
            
            

        }

class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['rut', 'nombre', 'direccion', 'email', 'telefono']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'direccion': 'Direccion', 
            'email': 'Email',
            'telefono': 'Telefono'
            
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direccion'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese email', 
                    'id': 'email'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese telefono', 
                    'id': 'telefono'
                }
            )  
            

        }

class PedidoForm(forms.ModelForm):

    class Meta: 
        model= Pedido
        fields = ['idProducto', 'rut', 'estado']
        labels ={
            'idProducto': 'Id_Producto', 
            'rut': 'Rut', 
            'estado': 'Estado'            
            
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Id Producto', 
                    'id': 'idProducto'
                }
            ), 
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ),
            'estado': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Estado Producto', 
                    'id': 'estado'
                }
            )            

        }
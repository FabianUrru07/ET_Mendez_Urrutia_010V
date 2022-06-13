
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import  Producto, Cliente



    

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        imagen  = forms.ImageField()
        imagen.widget.attrs.update({'class': 'form-control','id':'id_imagen'})
        fields = ['idProducto', 'nombre', 'precio','descripcion','imagen']
        labels ={
            'IdProducto': 'Id', 
            'nombre': 'Nombre', 
            'precio': 'Precio', 
            'descripcion': 'Descripcion',
            'imagen' : 'Imagen'
            
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
            
            

        }

class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['rut', 'nombre', 'apellido', 'email', 'telefono']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'apellido': 'Apellido', 
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
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese apellido', 
                    'id': 'apellido'
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
from django.shortcuts import redirect, render
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm
from django.contrib.auth import logout

# Create your views here.

def index(request):

    return render(request, 'index.html')


def ver(request):
    return render (request, 'registro.html')

def cont(request):
    return render (request, 'contacto.html')

def gale(request):
    return render (request, 'galeria.html')

def somos(request):
    return render (request, 'somos.html')

def api(request):
    return render (request, 'Api.html')
    
def form_crear_producto(request):
    
    if request.method=='POST':
        producto_form = ProductoForm(request.POST,request.FILES)
        
        if producto_form.is_valid():
            print("ENTRE2")
            producto_form.save()        #similar al insert
            return redirect('mostrarProducto')
    else:
        producto_form=ProductoForm()
    return render(request, 'form_crear_producto.html', {'producto_form': producto_form})

def form_mod_producto(request, id):
    producto =Producto.objects.get(idProducto=id)
    datos = {
        'form': ProductoForm(instance = producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('mostrarProducto')
    return render(request, 'form_mod_producto.html', datos)


def form_del_producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect('mostrarProducto')

def mostrarProducto(request):

    producto = Producto.objects.all()
    datos = {
        'producto' : producto
    }
    return render(request, 'mostrarProducto.html', datos)

def form_crear_cliente(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()        #similar al insert
            return redirect('mostrarCliente')
    else:
        cliente_form=ClienteForm()
    return render(request, 'form_crear_cliente.html', {'cliente_form': cliente_form})

def form_mod_cliente(request, id):
    cliente =Cliente.objects.get(rut=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('mostrarCliente')
    return render(request, 'form_mod_cliente.html', datos)


def form_del_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('mostrarCliente')

def mostrarCliente(request):

    cliente = Cliente.objects.all()
    datos = {
        'cliente' : cliente
    }
    return render(request, 'mostrarCliente.html', datos)



def salir(request):
    logout(request)
    return render(request,'index.html')
from django.shortcuts import redirect, render
from .models import Producto, Cliente, Pedido
from .forms import ProductoForm, ClienteForm, PedidoForm
from django.contrib.auth import logout

# Create your views here.

def test (request):
    return render(request, 'test.html')

def index(request):

    return render(request, 'index.html')

def ver(request):
    return render (request, 'registro.html')

def cont(request):
    return render (request, 'contacto.html')

def gale(request):
    producto = Producto.objects.all()
    datos = {
        'producto' : producto
    }

    return render (request, 'galeria.html',datos)

def ver_pedidos(request):
    pedido = Pedido.objects.all()
    datos = {
        'pedido' : pedido
    }

    return render (request, 'ver_pedidos.html',datos)

def pedidos_realizados(request,id):
    pedido = Pedido.objects.get(rut = id)
    producto = Producto.objects.get(idProducto = pedido.idProducto)
    datos = {
        'producto': producto,
        'pedido': pedido
    }

    return render(request,'pedidos_realizados.html',datos)
    

def somos(request):
    return render (request, 'somos.html')

def api(request):
    return render (request, 'Api.html')

def Detalle(request, id):
    producto = Producto.objects.get(idProducto = id)
    datos = {
        'producto': producto
    }
    return render(request,'Detalle_producto.html',datos)
    
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

def crear_pedido(request):
    
    if request.method=='POST':
        pedido_form = PedidoForm(request.POST)
        if pedido_form.is_valid():
            pedido_form.save()     
            return redirect('mostrarPedido')   #similar al insert
    else:
        pedido_form=PedidoForm()
    return render(request, 'form_crear_producto.html', {'pedido_form': pedido_form})
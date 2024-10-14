from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Cliente, Producto
from .forms import ClienteForm,ProductoForm
# Create your views here.
def primero(request):
    return render(request,'index.html')

def inicio(request):
    return render(request,'index.html')

def compra(request):
    return render(request,'compra_producto.html')

def vcliente(request):
    clientes=Cliente.objects.all()
    return render(request,'clientes.html',{'clientes': clientes})

def cliente(request):
    formulario=ClienteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('vcliente')
    return render(request,'form.html',{'formulario':formulario})

def actualizar(request,id):
    cliente=Cliente.objects.get(id=id)
    formulario=ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('vcliente')
    return render(request,'actualizar.html',{'formulario':formulario})

def eliminar(request,id):
    cliente=Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('vcliente')

def vproducto(request):
    productos=Producto.objects.all()
    return render(request,'productos.html',{'productos': productos})

def rtenis(request):
    formulario1=ProductoForm(request.POST or None, request.FILES or None )
    if formulario1.is_valid():
        formulario1.save()
        return redirect('vproducto')
    return render(request,'Rtenis.html',{'formulario1':formulario1})

def eliminarp(request,id):
    producto=Producto.objects.get(id=id)
    producto.delete()
    return redirect('vproducto')

def actualizarp(request,id):
    producto=Producto.objects.get(id=id)
    formulario1=ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario1.is_valid() and request.POST:
        formulario1.save()
        return redirect('vproducto')
    return render(request,'actualizarp.html',{'formulario1':formulario1})
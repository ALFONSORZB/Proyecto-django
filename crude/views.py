from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Cliente, Producto
from .forms import ClienteForm,ProductoForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def primero(request):
    return render(request,'index.html')

def regis(request):
    if request.method=='GET':
        return render(request,'signup.html',{
            'form':UserCreationForm
        })
    elif request.POST['password1'] == request.POST['password2']:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
        user.save()
        return redirect ('sigin')
    else:
        return HttpResponse("Contrasenas no coinciden")

def sigin(request):

    if request.method=='GET':
        return render(request,'sigin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request,'sigin.html',{
            'form': AuthenticationForm
            })
        else:
            login(request,user)
            return redirect ('inicio')

def salir(request):
    logout(request)
    return redirect('sigin')

@login_required
def inicio(request):
    return render(request,'index.html')
    
@login_required
def compra(request):
    return render(request,'compra_producto.html')
    
@login_required
def vcliente(request):
    clientes=Cliente.objects.all()
    return render(request,'clientes.html',{'clientes': clientes})
    
@login_required
def cliente(request):
    formulario=ClienteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('vcliente')
    return render(request,'form.html',{'formulario':formulario})
    
@login_required
def actualizar(request,id):
    cliente=Cliente.objects.get(id=id)
    formulario=ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('vcliente')
    return render(request,'actualizar.html',{'formulario':formulario})
    
@login_required
def eliminar(request,id):
    cliente=Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('vcliente')
    
@login_required
def vproducto(request):
    productos=Producto.objects.all()
    return render(request,'productos.html',{'productos': productos})
    
@login_required
def rtenis(request):
    formulario1=ProductoForm(request.POST or None, request.FILES or None )
    if formulario1.is_valid():
        formulario1.save()
        return redirect('vproducto')
    return render(request,'Rtenis.html',{'formulario1':formulario1})
    
@login_required
def eliminarp(request,id):
    producto=Producto.objects.get(id=id)
    producto.delete()
    return redirect('vproducto')
    
@login_required
def actualizarp(request,id):
    producto=Producto.objects.get(id=id)
    formulario1=ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario1.is_valid() and request.POST:
        formulario1.save()
        return redirect('vproducto')
    return render(request,'actualizarp.html',{'formulario1':formulario1})
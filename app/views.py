from django.shortcuts import render, get_object_or_404, redirect
from .models import Categorias, Producto, Producto_modelo
from .forms import EditModeloForm, CreateModeloForm, EditarProductoForm

def get_global_data():
    categorias = Categorias.objects.all()
    return {
        "categorias": categorias
    }
# Create your views here.
def index(request):
    context = get_global_data()
    cat_iphone = Categorias.objects.get(nombre="iPhone")
    iphones = Producto.objects.filter(categoria=cat_iphone)
    cat_mac = Categorias.objects.get(nombre="Mac")
    macs = Producto.objects.filter(categoria=cat_mac)
    cat_watch = Categorias.objects.get(nombre="Watch")
    watch = Producto.objects.filter(categoria=cat_watch)
    cat_pad = Categorias.objects.get(nombre="iPad")
    pad = Producto.objects.filter(categoria=cat_pad)
    cat_tyc = Categorias.objects.get(nombre="TV y Casa")
    tyc = Producto.objects.filter(categoria=cat_tyc)
    cat_pods = Categorias.objects.get(nombre="AirPods")
    pod = Producto.objects.filter(categoria=cat_pods)
    context.update({
        "iphones": iphones,
        "macs": macs,
        "watchs": watch,
        "pads": pad,
        "tycs": tyc,
        "pods": pod,
    })
    return render(request, 'index.html', context)

def temas(request, tema):
    context = get_global_data()
    categoria = Categorias.objects.get(nombre=tema)
    info = Producto.objects.filter(categoria=categoria)
    context.update({
        "categoria": categoria,
        "infom": info,
    })
    return render(request, 'tema.html', context)

def producto(request, tema, id_prod):
    context = get_global_data()
    prod = Producto.objects.get(id=id_prod)
    variantes = Producto_modelo.objects.filter(producto=prod)
    context.update({
        "producto": prod,
        "variantes": variantes
    })
    return render(request, 'producto.html', context)

def variante(request, tema, id_prod, id_variante):
    context = get_global_data()
    prod_select = Producto_modelo.objects.get(id=id_variante)
    prod = Producto.objects.get(id=id_prod)
    variantes = Producto_modelo.objects.filter(producto=prod)
    context.update({
        "producto": prod,
        "variantes": variantes,
        "variante_selec": prod_select
    })
    return render(request, 'subproducto.html', context)

def editar_producto_variante(request, id_modelo):
    context = get_global_data()
    prod_select = Producto_modelo.objects.get(id=id_modelo)
    prod_original = Producto.objects.get(id=prod_select.producto.id)
    stock_anterior = prod_select.stock

    if request.method == 'POST':
        form = EditModeloForm(request.POST, request.FILES, instance=prod_select)
        
        if form.is_valid():
            prod_original.stock -= stock_anterior

            nuevo_stock = int(request.POST.get('stock'))
            prod_original.stock += nuevo_stock

            prod_original.save()

            form.save()
            return redirect('index')
    else:
        form = EditModeloForm(instance=prod_select)

    context.update({
        "modelo": prod_select,
        "form": form
    })

    return render(request, 'edit_var.html', context)

def crear_variante(request, id_modelo):
    context = get_global_data()
    
    producto = get_object_or_404(Producto, id=id_modelo)
    
    if request.method == 'POST':
        form = CreateModeloForm(request.POST, request.FILES)
        if form.is_valid():
            stock = request.POST.get('stock')
            producto.stock += stock
            producto.save()
            form.save()
            return redirect('index')
    else:
        form = CreateModeloForm(initial={'producto': producto})
    
    context.update({
        "form": form
    })

    return render(request, 'crear_mod.html', context)

def editar_producto(request, id_prod):
    context = get_global_data()
    producto_editar = get_object_or_404(Producto, id=id_prod)
    if request.method == 'POST':
        form = EditarProductoForm(request.POST, request.FILES, instance=producto_editar)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditarProductoForm(instance=producto_editar)
    context.update({
        "form": form
    })
    return render(request, 'editar_prod.html', context)

def crear_producto(request, id_tema):
    context = get_global_data()
    tema = get_object_or_404(Categorias, id=id_tema)
    if request.method == 'POST':
        form = EditarProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditarProductoForm(initial={'categoria': tema})
    context.update({
        "form": form
    })
    return render(request, 'crear_producto.html', context)

def eliminar_producto(request, id_prod):
    producto_eliminar = get_object_or_404(Producto, id=id_prod)
    producto_eliminar.delete()
    return redirect('index')

def eliminar_variante(request, id_variante):
    subproducto_eliminar = get_object_or_404(Producto_modelo, id=id_variante)
    subproducto_eliminar.producto.stock -= subproducto_eliminar.stock
    subproducto_eliminar.delete()
    return redirect('index')
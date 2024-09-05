from django.shortcuts import render
from .models import Categorias, Producto


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
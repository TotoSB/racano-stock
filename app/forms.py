from django import forms
from .models import Producto_modelo, Producto

class EditModeloForm(forms.ModelForm):
    class Meta:
        model = Producto_modelo
        fields = [ 'nombre_variante', 'descripcion', 'image' , 'precio_proveedor', 'precio_unidad', 'stock']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

class CreateModeloForm(forms.ModelForm):
    class Meta:
        model = Producto_modelo
        fields = ['producto','nombre_variante', 'descripcion', 'image', 'precio_proveedor', 'precio_unidad', 'stock']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
    
class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['foto', 'nombre', 'descripcion', 'categoria']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
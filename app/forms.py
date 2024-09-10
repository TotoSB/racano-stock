from django import forms
from .models import Producto_modelo

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Producto_modelo
        fields = [ 'nombre_variante', 'descripcion', 'image' , 'precio_proveedor', 'precio_unidad', 'stock']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
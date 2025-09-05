from django import forms
from .models import Dispositivo

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ['nombre', 'consumo_maximo', 'estado', 'categoria', 'zona']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'consumo_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'zona': forms.Select(attrs={'class': 'form-select'}),
        }

        def clean_nombre(self):
            nombre = self.clean_data.get('nombre') 
            # valor ingresado por el usuario clanead_data es un diccionario

            if len(nombre) < 3: # Verificar si el nombre tiene al menos 3 caracteres
                raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
            return nombre
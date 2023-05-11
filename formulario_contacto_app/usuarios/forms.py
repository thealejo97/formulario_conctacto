from django import forms
from .models import Usuario
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class UsuarioForm(forms.ModelForm):
    fecha_de_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'))

    class Meta:
        model = Usuario
        fields = [
            'genero',
            'fecha_de_nacimiento',
            'nombre',
            'apellido',
            'email',
            'direccion',
            'casa_apto',
            'pais',
            'region',
            'ciudad',
            'descripcion'
        ]

        widgets = {
            'genero': forms.Select(attrs={'placeholder': 'Selecciona tu género'})

        }

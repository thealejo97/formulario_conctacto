from datetime import timedelta, date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Usuario
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class UsuarioForm(forms.ModelForm):
    fecha_de_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'))

    def clean_fecha_de_nacimiento(self):
        fecha_de_nacimiento = self.cleaned_data['fecha_de_nacimiento']
        edad = (date.today() - fecha_de_nacimiento) // timedelta(days=365.2425)

        if edad < 18:
            raise ValidationError(_('Debes tener 18 años para usar la plataforma.'))

        return fecha_de_nacimiento

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

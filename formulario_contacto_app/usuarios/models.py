from django.db import models
from cities_light.models import Country, City, Region
from django.core.validators import EmailValidator


class Usuario(models.Model):
    GENEROS = (
        ("F", "Femenino"),
        ("M", "Masculino"),
        ("O", "Otra"),
        ("N", "Preferiría no contestar"),
    )

    genero = models.CharField(max_length=10, choices=GENEROS, verbose_name='Sexo*')
    fecha_de_nacimiento = models.DateField(verbose_name='Fecha de nacimiento*')
    nombre = models.CharField(max_length=50, verbose_name="Nombre*", unique=True)
    apellido = models.CharField(max_length=50, verbose_name="Apellido*", unique=True)
    email = models.CharField(verbose_name="Email", max_length=200, blank=True, null=True, validators=[EmailValidator('Correo electrónico inválido')])

    pais = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='pais',
                             verbose_name="País*", default=1)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='region',
                               verbose_name="Departamento*")
    ciudad = models.ForeignKey(City, on_delete=models.PROTECT, related_name='ciudad',
                               verbose_name="Ciudad*")
    direccion = models.CharField(max_length=100, verbose_name="Dirección*")
    casa_apto = models.CharField(max_length=100, verbose_name="Casa/Apto", blank=True, null=True)
    descripcion = models.CharField(max_length=100, verbose_name="Descripción", blank=True, null=True)


    activo = models.BooleanField(verbose_name="¿El tipo se encuentra activo?", default=True)
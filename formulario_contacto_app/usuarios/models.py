from django.db import models
from cities_light.models import Country, City, Region


class Usuario(models.Model):
    GENEROS = (
        ("F", "Femenino"),
        ("M", "Masculino"),
        ("O", "Otra"),
        ("N", "Preferiría no contestar"),
    )

    genero = models.CharField(max_length=10, choices=GENEROS, verbose_name='elige tu sexo*', null=True, blank=False)
    fecha_de_nacimiento = models.DateField(verbose_name='fecha de nacimiento*', null=True, blank=False)
    nombre = models.CharField(max_length=50, verbose_name="nombre*", unique=True)
    apellido = models.CharField(max_length=50, verbose_name="apellido*", unique=True)

    pais = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='pais',
                             verbose_name="¿En qué país se encuentra?*", default=1)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='region',
                               verbose_name="¿En qué región se encuentra?*", null=True, blank=False)
    ciudad = models.ForeignKey(City, on_delete=models.PROTECT, related_name='ciudad',
                               verbose_name="¿En qué ciudad se encuentra?*", null=True, blank=False)
    direccion = models.CharField(max_length=100, verbose_name="dirección donde se reúnen frecuentemente", blank=True)
    casa_apto = models.CharField(max_length=100, verbose_name="dirección donde se reúnen frecuentemente", blank=True)
    descripcion = models.CharField(max_length=100, verbose_name="dirección donde se reúnen frecuentemente", blank=True)


    activo = models.BooleanField(verbose_name="¿El tipo se encuentra activo?", default=True)
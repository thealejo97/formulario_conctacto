from django.urls import path
from .views import *

app_name = "usuarios"

urlpatterns = [
    path('usuario/formulario/', view=UsuarioRegistrar.as_view(), name='listado_rutas')
]
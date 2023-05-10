from django.urls import path
from .views import *

app_name = "usuarios"

urlpatterns = [
    path('registrar/', view=UsuarioRegistrar.as_view(), name='crear_usuario')
]
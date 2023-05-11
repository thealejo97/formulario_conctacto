from django.urls import path
from .views import *

app_name = "usuarios"

urlpatterns = [
    path('list/', view=UsuarioApiList.as_view(), name='listar_usuarios')
]
from django.views.generic import CreateView
# Modulos internos de la app
from .forms import UsuarioForm
from .models import Usuario
from .serializers import UsuariosSerializer
from django.urls import reverse_lazy

class UsuarioRegistrar(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuarios/registrar.html"
    success_url = reverse_lazy('usuarios:crear_usuario')

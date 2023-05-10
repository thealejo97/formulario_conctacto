from django.views.generic import CreateView, UpdateView, DetailView, TemplateView, ListView, FormView, DeleteView
# Modulos internos de la app
from .forms import UsuarioForm
from .models import Usuario
from .serializers import UsuariosSerializer

class UsuarioRegistrar(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuarios/registrar.html"

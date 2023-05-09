from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView, ListView, FormView, DeleteView
# Modulos internos de la app
from .forms import UsuarioForm
from .models import Usuario
from .serializers import UsuariosSerializer

class UsuarioRegistrar(LoginRequiredMixin, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuario/registrar.html"

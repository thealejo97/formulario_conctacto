from rest_framework import generics
from formulario_contacto_app.usuarios.models import Usuario
from formulario_contacto_app.usuarios.serializers import UsuariosSerializer


class UsuarioApiList(generics.ListAPIView):

    serializer_class = UsuariosSerializer

    def get_queryset(self):
        print(Usuario.objects.all())
        return  Usuario.objects.all()
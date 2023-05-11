from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Count
from formulario_contacto_app.usuarios.models import Usuario
from formulario_contacto_app.usuarios.serializers import UsuariosSerializer


class UsuarioApiList(generics.ListAPIView):

    serializer_class = UsuariosSerializer

    def get_queryset(self):
        return  Usuario.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        response_data = {
            'total_usuarios': Usuario.objects.all().count(),
            'usuarios_por_ciudad': queryset.values('ciudad__name').annotate(usuarios_por_ciudad=Count('ciudad')).order_by('-usuarios_por_ciudad'),
            'usuarios': serializer.data,

        }

        return Response(response_data)
from rest_framework import serializers
from .models import Usuario

class UsuariosSerializer(serializers.ModelSerializer):


    class Meta:
        model = Usuario
        fields = []
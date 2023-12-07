from rest_framework import serializers #esta biblioteca es una extencion del framework Django que proporciona herramientas y utilidades adicionales para construir APIs web

from .models import Proyect

class ProyectSeializer(serializers.ModelSerializer):
    class Meta:
        model = Proyect
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)
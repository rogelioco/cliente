from rest_framework import routers, serializers, viewsets
from Profile.models import Profile, Ciudad, Genero, Ocupacion, Estado, EstadoCivil

class EstadoCivilSerializers(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        # fields = ('nombre', 'apellidoPaterno', 'apellidoMaterno', 'edad')
        fields = ('__all__')

class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estado
        # fields = ('nombre', 'apellidoPaterno', 'apellidoMaterno', 'edad')
        fields = ('__all__')

class OcupacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        # fields = ('nombre', 'apellidoPaterno', 'apellidoMaterno', 'edad')
        fields = ('__all__')

class GeneroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genero
        # fields = ('nombre', 'apellidoPaterno', 'apellidoMaterno', 'edad')
        fields = ('__all__')

class CiudadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        # fields = ('nombre', 'apellidoPaterno', 'apellidoMaterno', 'edad')
        fields = ('__all__')

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = ('nombre', 'apellidoPaterno', 'apellidoMaterno', 'edad')
        fields = ('__all__')
from django.db import models
from django.utils import timezone
# Create your models here.


class EstadoCivil(models.Model):
    estado = models.CharField(max_length = 254, null = False)
    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.estado

    class Meta:
        db_table = 'EstadoCivil'

class Estado(models.Model):
    nombre = models.CharField(max_length = 254, null = False)
    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Estado'

class Ocupacion(models.Model):
    ocupacion = models.CharField(max_length = 254, null = False)
    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.ocupacion

    class Meta:
        db_table = 'Ocupacion'


class Genero(models.Model):
    sexo = models.CharField(max_length = 254, null = False)
    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.sexo

    class Meta:
        db_table = 'Genero'

class Ciudad(models.Model):
    nombre = models.CharField(max_length = 254, null = False)
    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Ciudad'


class Profile(models.Model):
    nombre = models.CharField(max_length = 254, null = False)
    apellidoPaterno = models.CharField(max_length = 254, null = False)
    apellidoMaterno = models.CharField(max_length = 254, null = False)
    edad = models.IntegerField(null = False)
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete = models.CASCADE)
    ocupacion = models.ForeignKey(Ocupacion, on_delete = models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete = models.CASCADE)
    estadoCivil = models.ForeignKey(EstadoCivil, on_delete = models.CASCADE)
    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Profile'



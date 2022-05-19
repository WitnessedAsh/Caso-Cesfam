from statistics import mode
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

class TIPO_USUARIO(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    NOM_TIPO_USU = models.CharField(max_length=50,verbose_name='Nombre del tipo de usuario')
    def getTipo(id):
        try:
            t=User.objects.get(pk=id)
            tipo = t.tipo_usuario.tipo
            return tipo
        except TIPO_USUARIO.DoesNotExist:
            return None
    def __str__(self):
        return self.NOM_TIPO_USU

class TUTOR(models.Model):
    rut_tutor = models.CharField(max_length=9,primary_key=True, verbose_name='Rut (sin punto ni guión) del paciente')
    nombre_tutor = models.CharField(max_length=50,verbose_name='Nombre del paciente')
    correo_tutor = models.CharField(null=True,blank=True,max_length=100,verbose_name='Mail')
    numero_tutor = models.IntegerField(null=True,blank=True,verbose_name='Teléfono')

    def __str__(self):
        return self.nombre_tutor

class PACIENTE(models.Model):
    rut_pac = models.CharField(max_length=9,primary_key=True, verbose_name='Rut (sin punto ni guión) del paciente')
    nombre_pac = models.CharField(max_length=50,verbose_name='Nombre del paciente')
    correo_pac = models.CharField(null=True,blank=True,max_length=100,verbose_name='Mail')
    numero_pac = models.IntegerField(null=True,blank=True,verbose_name='Teléfono')
    nombre_tutor = models.ForeignKey(TUTOR,null=True,blank=True,on_delete=models.CASCADE,verbose_name='Tutor')

    def __str__(self):
        return self.nombre_pac

class MEDICAMENTO(models.Model):
    id_medicamento = models.IntegerField(primary_key=True,verbose_name='Id de medicamento')
    nombre_medicamento = models.CharField(max_length=50,verbose_name='Nombre del medicamento')
    precio_medicamento = models.IntegerField(verbose_name='Precio del medicamento')
    stock_medicamento = models.IntegerField(verbose_name='Stock del medicamento')
    estado_medicamento = models.CharField(max_length=12,verbose_name='Estado del medicamento')
    gramos_medicamento = models.IntegerField(verbose_name='Gramos del medicamento')

    def __str__(self):
        return self.nombre_medicamento

class PRESCRIPCION(models.Model):
    id_prescripcion = models.IntegerField(primary_key=True,verbose_name='Id de la prescripcion')
    desc_prescripcion = models.CharField(max_length=500,verbose_name='Descripcion de la prescripcion')
    fecha_emision = models.DateField(null=True,blank=True,verbose_name='Fecha de emision')
    Username = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Medico')
    rut_pac = models.ForeignKey(PACIENTE,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Paciente')
    
    def __str__(self):
        return self.desc_prescripcion



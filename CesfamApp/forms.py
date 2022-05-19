from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import MEDICAMENTO, PRESCRIPCION, PACIENTE
from django.contrib.auth.models import User

class MEDICAMENTOFORM(ModelForm):
    class Meta:
        model = MEDICAMENTO
        fields = ['id_medicamento', 'nombre_medicamento', 'precio_medicamento', 'stock_medicamento','estado_medicamento','gramos_medicamento']

class PRESCRIPCIONFORM(ModelForm):
    class Meta:
        model = PRESCRIPCION
        fields = ['id_prescripcion', 'desc_prescripcion', 'fecha_emision', 'Username','rut_pac']

class PACIENTEFORM(ModelForm):
    class Meta:
        model = PACIENTE
        fields = ['rut_pac', 'nombre_pac', 'correo_pac', 'numero_pac']
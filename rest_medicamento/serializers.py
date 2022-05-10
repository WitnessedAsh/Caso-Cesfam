from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from CesfamApp.models import MEDICAMENTO, PRESCRIPCION

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MEDICAMENTO
        fields = ['id_medicamento','','']

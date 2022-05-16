from rest_framework import serializers
from CesfamApp.models import MEDICAMENTO, PRESCRIPCION, PACIENTE

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MEDICAMENTO
        fields = ['id_medicamento','nombre_medicamento','precio_medicamento','stock_medicamento','estado_medicamento','gramos_medicamento']


class PrescripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRESCRIPCION
        fields = ['id_prescripcion','desc_prescripcion','fecha_emision','medico','nombre_paciente']

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PACIENTE
        fields = ['rut_pac','nombre_pac','correo_pac','numero_pac']

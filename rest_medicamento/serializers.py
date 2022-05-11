from rest_framework import serializers
from CesfamApp.models import MEDICAMENTO, PRESCRIPCION

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MEDICAMENTO
        fields = ['id_medicamento','nombre_medicamento','precio_medicamento','stock_medicamento','estado_medicamento','gramos_medicamento']


class PrescripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRESCRIPCION
        fields = ['id_prescripcion','desc_prescripcion','fecha_emision','medico','nombre_paciente']

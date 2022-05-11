from django.contrib import admin
from .models import MEDICAMENTO, PRESCRIPCION, TIPO_USUARIO, USUARIO, PACIENTE, TUTOR
# Register your models here.
admin.site.register(MEDICAMENTO)
admin.site.register(PRESCRIPCION)
admin.site.register(USUARIO)
admin.site.register(TIPO_USUARIO)
admin.site.register(PACIENTE)
admin.site.register(TUTOR)
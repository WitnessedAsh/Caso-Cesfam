from django.urls import path
from rest_medicamento.views import detalle_paciente, lista_medicamento, detalle_medicamento, lista_paciente, lista_prescripcion, detalle_prescripcion
from rest_medicamento.viewsLogin import loginapi

urlpatterns = [
    path('lista_medicamento',lista_medicamento,name='lista_medicamento'),
    path('detalle_medicamento/<id>',detalle_medicamento,name='detalle_medicamento'),
    path('lista_prescripcion',lista_prescripcion,name='lista_prescripcion'),
    path('detalle_prescripcion/<id>',detalle_prescripcion,name='detalle_prescripcion'),
    path('lista_paciente',lista_paciente,name='lista_paciente'),
    path('detalle_paciente/<id>',detalle_paciente,name='detalle_paciente'),
    path('loginapi',loginapi,name='loginapi'),
]
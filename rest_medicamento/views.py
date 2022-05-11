from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from CesfamApp.models import MEDICAMENTO, PRESCRIPCION
from .serializers import MedicamentoSerializer, PrescripcionSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# MEDICAMENTO #

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_medicamento(request):
    if request.method == 'GET':
        medicamento = MEDICAMENTO.objects.all()
        serializer = MedicamentoSerializer(medicamento, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MedicamentoSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_medicamento(request,id):
    try:
        medicamento = MEDICAMENTO.objects.get(id_medicamento=id)
    except MEDICAMENTO.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MedicamentoSerializer(medicamento)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MedicamentoSerializer(medicamento, data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        medicamento.delete()
        return Response(status=status.HTTP_204_NOT_CONTENT)

# PRESCRIPCION #

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_prescripcion(request):
    if request.method == 'GET':
        prescripcion = PRESCRIPCION.objects.all()
        serializer = PrescripcionSerializer(prescripcion, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PrescripcionSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_prescripcion(request,id):
    try:
        prescripcion = PRESCRIPCION.objects.get(id_prescripcion=id)
    except PRESCRIPCION.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PrescripcionSerializer(prescripcion)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PrescripcionSerializer(prescripcion, data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        prescripcion.delete()
        return Response(status=status.HTTP_204_NOT_CONTENT)
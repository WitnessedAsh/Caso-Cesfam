from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .models import MEDICAMENTO, PRESCRIPCION, PACIENTE, TUTOR, TIPO_USUARIO
from .forms import MEDICAMENTOFORM
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required 


# Create your views here.

def home(request):
    return render(request, 'CesfamWeb/index.html')

def listmedicamentos(request):
    return render(request, 'CesfamWeb/listmedicamentos.html')

def reserva(request):
    return render(request, 'CesfamWeb/reserva.html')   

def agregarmed(request):
    return render(request, 'Forms/form_medicamento.html') 


# --- MEDICAMENTO ---
#AGREGAR
def form_med(request):
    datos = {
        'form':MEDICAMENTOFORM()
    }
    if(request.method == 'POST'):
        formulario = MEDICAMENTOFORM(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado correctamente'
        else:
            formulario = MEDICAMENTOFORM()
            datos['mensaje'] = 'ERROR: No se ha guardado el producto, intente nuevamente'
    return render(request,'Forms/form_medicamento.html',datos)
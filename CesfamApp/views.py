from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .models import MEDICAMENTO, PRESCRIPCION, PACIENTE, TUTOR, TIPO_USUARIO
from .forms import MEDICAMENTOFORM, PRESCRIPCIONFORM, PACIENTEFORM
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required 


# Create your views here.

def home(request):
    return render(request, 'CesfamWeb/index.html')

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

#ELIMINAR
def form_del_medicamento(request, id):
    medicamento = MEDICAMENTO.objects.get(id_medicamento=id)
    medicamento.delete()

    return redirect(to='CesfamWeb/listmedicamentos.html')

#LIST
def listmedicamentos(request):
    medicamento = MEDICAMENTO.objects.all 
    datos = {
        'contacto': medicamento
    }
    return render(request,'CesfamWeb/listmedicamentos.html',datos)

# --- PRESCRIPCION ---
#AGREGAR
def form_pre(request):
    datos = {
        'form':PRESCRIPCIONFORM()
    }
    if(request.method == 'POST'):
        formulario = PRESCRIPCIONFORM(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado correctamente'
        else:
            formulario = PRESCRIPCIONFORM()
            datos['mensaje'] = 'ERROR: No se ha guardado el producto, intente nuevamente'
    return render(request,'Forms/',datos)

#ELIMINAR
def form_del_prescripcion(request, id):
    medicamento = PRESCRIPCION.objects.get(id_medicamento=id)
    medicamento.delete()

    return redirect(to='CesfamWeb/')

# --- PACIENTE ---
#AGREGAR
def form_pac(request):
    datos = {
        'form':PACIENTEFORM()
    }
    if(request.method == 'POST'):
        formulario = PACIENTEFORM(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado correctamente'
        else:
            formulario = PACIENTEFORM()
            datos['mensaje'] = 'ERROR: No se ha guardado el producto, intente nuevamente'
    return render(request,'Forms/',datos)
    
#ELIMINAR
def form_del_paciente(request, id):
    medicamento = PACIENTE.objects.get(id_medicamento=id)
    medicamento.delete()

    return redirect(to='CesfamWeb/')
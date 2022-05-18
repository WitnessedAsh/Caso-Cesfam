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

#def form_medicamento(request):
    return render(request, 'Forms/form_medicamento.html') 

def modificarmed(request):
    return render(request, 'Forms/form_mod_medicamento.html') 

def eliminarmed(request):
    return render(request, 'CesfamWeb/listmedicamentos.html') 

def agregarpre(request):
    return render(request, 'Forms/form_prescripcion.html') 

def modificarpre(request):
    return render(request, 'Forms/form_mod_prescripcion.html') 

def eliminarpre(request):
    return render(request, 'CesfamWeb/listprescripciones.html') 

def agregarpac(request):
    return render(request, 'Forms/form_paciente.html') 

def modificarpac(request):
    return render(request, 'Forms/form_mod_paciente.html') 

def eliminarpac(request):
    return render(request, 'CesfamWeb/listpacientes.html')         
# --- MEDICAMENTO ---
#AGREGAR
def form_med(request):
    datos = {
        'form':MEDICAMENTOFORM()
    }
    if request.method == 'GET':
        return render(request, "Forms/form_medicamento.html")
    if(request.method == 'POST'):
        formulario = MEDICAMENTOFORM(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado correctamente'
        else:
            formulario = MEDICAMENTOFORM()
            datos['mensaje'] = 'ERROR: No se ha guardado el producto, intente nuevamente'
    return render(request,'Forms/form_medicamento.html',datos)

def form_medicamento(request):
    if request.method == 'GET':
        return render(request, "Forms/form_medicamento.html")
    if request.method == 'POST':
        id_medicamento	= request.POST['IDmed']
        nombre_medicamento = request.POST['NOMmed'] 
        precio_medicamento = request.POST['PREmed'] 
        stock_medicamento	= request.POST['STOmed'] 
        estado_medicamento = request.POST['ESTmed'] 
        gramos_medicamento = request.POST['GRMmed']
        medicamento = MEDICAMENTO.objects.create(id_medicamento=id_medicamento, nombre_medicamento=nombre_medicamento, precio_medicamento=precio_medicamento, stock_medicamento=stock_medicamento, estado_medicamento=estado_medicamento, gramos_medicamento=gramos_medicamento)

#MODIFICAR
def form_mod_med(request,id):
    medicamento = MEDICAMENTO.objects.get(id_medicamento = id)
    datos = {
        'form':MEDICAMENTOFORM(instance=medicamento)
    }
    if(request.method == 'POST'):
        formulario = MEDICAMENTOFORM(request.POST, request.FILES,instance=medicamento)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modicado correctamente'
        else:
            formulario = MEDICAMENTOFORM()
            datos['mensaje'] = 'ERROR: No se ha modicado el producto, intente nuevamente'
    return render(request,'Forms/form_mod_medicamento.html',datos)

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

#--De prueba-- Si se consigue base de dato
#def listmedicamentos(request):
#    medicamento = MEDICAMENTO.objects.raw('SELECT * FROM (MODELO) order by id)
#    datos = {
#        'contacto': medicamento
#    }
#    return render(request,'CesfamWeb/listmedicamentos.html',datos)

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
            datos['mensaje'] = 'ERROR: No se ha guardado la prescripcion, intente nuevamente'
    return render(request,'Forms/form_prescripcion.html',datos)

#MODIFICAR
def form_mod_pre(request,id):
    prescripcion = PRESCRIPCION.objects.get(id_prescripcion = id)
    datos = {
        'form':PRESCRIPCIONFORM(instance=prescripcion)
    }
    if(request.method == 'POST'):
        formulario = PRESCRIPCIONFORM(request.POST, request.FILES, instance=prescripcion)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modicado correctamente'
        else:
            formulario = PRESCRIPCIONFORM()
            datos['mensaje'] = 'ERROR: No se ha modicado la prescripcion, intente nuevamente'
    return render(request,'Forms/form_mod_prescripcion.html',datos)

#ELIMINAR
def form_del_prescripcion(request, id):
    prescripcion = PRESCRIPCION.objects.get(id_prescripcion=id)
    prescripcion.delete()

    return redirect(to='CesfamWeb/listprescripciones.html')

#LIST
def listprescripciones(request):
    prescripcion = PRESCRIPCION.objects.all
    datos = {
        'contacto': prescripcion
    }
    return render(request,'CesfamWeb/listprescripciones.html',datos)

#--De prueba-- Si se consigue base de dato
#def listprescripciones(request):
#    prescripcion = PRESCRIPCION.objects.objects.raw('SELECT * FROM (MODELO) order by id')
#    datos = {
#        'contacto': prescripcion
#    }
#    return render(request,'CesfamWeb/listprescripciones.html',datos)
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
            datos['mensaje'] = 'ERROR: No se ha guardado al paciente, intente nuevamente'
    return render(request,'Forms/form_paciente.html',datos)

def form_mod_pac(request,id):
    paciente = PACIENTE.objects.get(rut_pac = id)
    datos = {
        'form':PACIENTEFORM(instance=paciente)
    }
    if(request.method == 'POST'):
        formulario = PACIENTEFORM(request.POST, request.FILES,instance=paciente)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modicado correctamente'
        else:
            formulario = PACIENTEFORM()
            datos['mensaje'] = 'ERROR: No se ha modicado al paciente, intente nuevamente'
    return render(request,'Forms/form_mod_paciente.html',datos)

#ELIMINAR
def form_del_paciente(request, id):
    paciente = PACIENTE.objects.get(rut_pac=id)
    paciente.delete()

    return redirect(to='CesfamWeb/listpacientes.html')

#LIST
def listpacientes(request):
    paciente = PRESCRIPCION.objects.all
    datos = {
        'contacto': paciente
    }
    return render(request,'CesfamWeb/listpacientes.html',datos)

#--De prueba-- Si se consigue base de dato
#def listpacientes(request):
#    paciente = PRESCRIPCION.objects.objects.raw('SELECT * FROM (MODELO) order by id')
#    datos = {
#        'contacto': paciente
#    }
#    return render(request,'CesfamWeb/listpacientes.html',datos)
    
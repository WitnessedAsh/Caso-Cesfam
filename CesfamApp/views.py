from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .models import MEDICAMENTO, PRESCRIPCION, PACIENTE, TUTOR, TIPO_USUARIO
from .forms import MEDICAMENTOFORM, PRESCRIPCIONFORM, PACIENTEFORM
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required 
from django.core.mail import send_mail
import datetime

# Create your views here.

def home(request):
    return render(request, 'CesfamWeb/index.html')

def reserva(request):
    return render(request, 'CesfamWeb/reserva.html')   

#def form_medicamento(request):
    #return render(request, 'Forms/form_medicamento.html') 

#def modificarmed(request):
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
        medicamento = MEDICAMENTO.objects.create(
            id_medicamento=id_medicamento, 
            nombre_medicamento=nombre_medicamento, 
            precio_medicamento=precio_medicamento, 
            stock_medicamento=stock_medicamento, 
            estado_medicamento=estado_medicamento, 
            gramos_medicamento=gramos_medicamento)
        return redirect('form_medicamento')

#MODIFICAR
def form_mod_medicamento(request, id_medicamento):
    if request.method == 'GET':
        modMed = MEDICAMENTO.objects.get(id_medicamento=id_medicamento)
        return render(request, "Forms/form_mod_medicamento.html", {"MEDICAMENTO": modMed})
    elif request.method == 'POST':
        precio_medicamento = request.POST['PREmed'] 
        stock_medicamento	= request.POST['STOmed'] 
        estado_medicamento = request.POST['ESTmed'] 

        medicamento = MEDICAMENTO.objects.get(id_medicamento=id_medicamento)
        medicamento.precio_medicamento = precio_medicamento
        medicamento.stock_medicamento = stock_medicamento
        medicamento.estado_medicamento = estado_medicamento
        medicamento.save()  

        return redirect('form_mod_medicamento')

#ELIMINAR
def form_del_medicamento(request, id_medicamento):
    medicamento = MEDICAMENTO.objects.get(id_medicamento=id_medicamento)
    medicamento.delete()

    return redirect(to='CesfamWeb/listmedicamentos.html')

#LIST
def listmedicamentos(request):
    medicamento = MEDICAMENTO.objects.all
    datos = {
        'contacto': medicamento
    }
    return render(request,'CesfamWeb/listmedicamentos.html',datos)

#AVISAR
def AvisoMedicamento(request, rut_pac):
    if request.method == 'GET':
        paciente = PACIENTE.objects.get(rut_pac=rut_pac)
        return render(request, "farmacia/recepcion_entrega.html", {"paciente": paciente})

    if request.method == 'POST':
        nombre_pac = request.POST['NOMPac']
        correo = request.POST['msgEmail']

        #fecha = datetime.datetime.now()
        #fechastr =  fecha.strftime("%m/%d/%Y, %H:%M:%S")
        subject = 'Receta entregada a '+paciente
        message = 'Saludos '+nombre_pac+' este correo es para avisarle que sus medicamentos se encuentran disponibles'
        email_from = 'farmaciapruebacesfam@gmail.com'
        email_to_list = [correo]
        send_mail(subject,message,email_from, email_to_list)

        return redirect('recepcion-farmacia')

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
    if request.method == 'GET':
        return render(request, "Forms/form_prescripcion.html")
    if request.method == 'POST':
        id_prescripcion	= request.POST['IDpre']
        desc_prescripcion = request.POST['DESCpre'] 
        fecha_emision = request.POST['DATEpre'] 
        medico	= request.POST['MEDpre'] 
        nombre_pac = request.POST['PACpre']

        prescripcion = PACIENTE.objects.create(
            id_prescripcion=id_prescripcion, 
            desc_prescripcion=desc_prescripcion, 
            fecha_emision=fecha_emision, 
            medico=medico,
            nombre_pac=nombre_pac)
        return redirect('form_prescripcion')

#MODIFICAR
def form_mod_pre(request,id_prescripcion):
    if request.method == 'GET':
        return render(request, "Forms/form_mod_prescripcion.html")
    if request.method == 'POST':
        desc_prescripcion = request.POST['DESCpre'] 

        prescripcion = PRESCRIPCION.objects.get(id_prescripcion=id_prescripcion)
        prescripcion.desc_prescripcion = desc_prescripcion
        prescripcion.save()  

        return redirect('form_mod_prescripcion')

#ELIMINAR
def form_del_prescripcion(request, id_prescripcion):
    prescripcion = PRESCRIPCION.objects.get(id_prescripcion=id_prescripcion)
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
def form_paciente(request):
    if request.method == 'GET':
        return render(request, "Forms/form_paciente.html")
    if request.method == 'POST':
        rut_pac	= request.POST['RUT']
        nombre_pac = request.POST['NOMpac'] 
        correo_pac = request.POST['EMAIL'] 
        numero_pac	= request.POST['NUM'] 

        paciente = PACIENTE.objects.create(
            rut_pac=rut_pac, 
            nombre_pac=nombre_pac, 
            correo_pac=correo_pac, 
            numero_pac=numero_pac)
        return redirect('form_paciente')

def form_mod_pac(request,rut_pac):
    if request.method == 'GET':
        modPAC = PACIENTE.objects.get(rut_pac=rut_pac)
        return render(request, "Forms/form_paciente.html", {"PACIENTE": modPAC})
    if request.method == 'POST':
        nombre_pac = request.POST['NOMpac'] 
        correo_pac = request.POST['EMAIL'] 
        numero_pac	= request.POST['NUM'] 

        paciente = PACIENTE.objects.get(rut_pac=rut_pac)
        paciente.nombre_pac = nombre_pac
        paciente.correo_pac = correo_pac
        paciente.numero_pac = numero_pac
        paciente.save()  

        return redirect('form_mod_paciente')

#ELIMINAR
def form_del_paciente(request, rut_pac):
    paciente = PACIENTE.objects.get(rut_pac=rut_pac)
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
    
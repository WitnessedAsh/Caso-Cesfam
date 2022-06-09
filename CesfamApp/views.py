from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .models import MEDICAMENTO, PRESCRIPCION, PACIENTE, TUTOR, TIPO_USUARIO
from .forms import MEDICAMENTOFORM, PRESCRIPCIONFORM, PACIENTEFORM
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required 
from django.core.mail import send_mail
import os
from twilio.rest import Client
import datetime
account_sid = 'AC6d57e3063cd5c1f3ad933c4158bfb26d'
auth_token = '7a47704f136015e9756ba0020b75dd20'
client = Client(account_sid, auth_token)
# Create your views here.

def home(request):
    return render(request, 'CesfamWeb/index.html')

def reserva(request):
    return render(request, 'CesfamWeb/reserva.html')   
     
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
        return redirect('listmedicamentos')

#MODIFICAR
def form_mod_medicamento(request, id):
    if request.method == 'GET':
        modMed = MEDICAMENTO.objects.get(id_medicamento=id)
        return render(request, "Forms/form_mod_medicamento.html", {"MEDICAMENTO": modMed})
    elif request.method == 'POST':
        id_medicamento	= request.POST['IDmed']
        nombre_medicamento = request.POST['NOMmed'] 
        precio_medicamento = request.POST['PREmed'] 
        stock_medicamento	= request.POST['STOmed'] 
        estado_medicamento = request.POST['ESTmed'] 
        gramos_medicamento = request.POST['GRMmed']
        medicamento = MEDICAMENTO.objects.get(id_medicamento=id_medicamento)
        medicamento.id_medicamento = id_medicamento
        medicamento.nombre_medicamento = nombre_medicamento
        medicamento.precio_medicamento = precio_medicamento
        medicamento.stock_medicamento = stock_medicamento
        medicamento.estado_medicamento = estado_medicamento
        medicamento.gramos_medicamento = gramos_medicamento
        medicamento.save()  
        return redirect('listmedicamentos')

#ELIMINAR
def form_del_medicamento(request, id):
    medicamento = MEDICAMENTO.objects.get(id_medicamento=id)
    medicamento.delete()

    return redirect(to='listmedicamentos')

#LIST
def listmedicamentos(request):
    medicamento = MEDICAMENTO.objects.all
    datos = {
        'medicamento': medicamento
    }
    return render(request,'CesfamWeb/listmedicamentos.html',datos)  

#AVISAR
def notificarPac(request, rut_pac):
    if request.method == 'GET':
        paciente = PACIENTE.objects.get(rut_pac=rut_pac)
        return render(request, "Forms/notificarPac.html", {"PACIENTE": paciente})
    if request.method == 'POST':
        nombre_pac = request.POST['NOMpac']
        correo = request.POST['EMAIL']
        subject = 'Aviso de medicamentos para '+ nombre_pac
        message = 'Saludos '+ nombre_pac+' este correo es para avisarle que sus medicamentos se encuentran disponibles'
        email_from = 'farmaciapruebacesfam@gmail.com'
        email_to_list = [correo]
        send_mail(subject,message,email_from, email_to_list)
        return redirect('listpacientes')

#AVISO WSP
def twiliowsp(request, rut_pac):
    if request.method == 'GET':
        paciente = PACIENTE.objects.get(rut_pac=rut_pac)
        return render(request, "Forms/twiliowsp.html", {"PACIENTE": paciente})
    if request.method == 'POST':
        nombre_pac = request.POST['NOMpac']
        numero = request.POST['NUMpac']
        message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Saludos '+nombre_pac+' este mensaje es para avisarle que sus medicamentos se encuentran disponibles',
                              to='whatsapp:'+numero
                          )
        print(message.sid)
        return redirect('listpacientes')

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
        Username = request.POST['User'] 
        nombre_pac = request.POST['PACpre']
        prescripcion = PRESCRIPCION.objects.create(
            id_prescripcion=id_prescripcion, 
            desc_prescripcion=desc_prescripcion, 
            fecha_emision=fecha_emision, 
            Username=Username,
            nombre_pac=nombre_pac)
        return redirect('listprescripciones')

#MODIFICAR
def form_mod_pre(request,id):
    if request.method == 'GET':
        prescripcion = PRESCRIPCION.objects.get(id_prescripcion=id)
        return render(request, "Forms/form_mod_prescripcion.html", {"PRESCRIPCION": prescripcion})
    if request.method == 'POST':
        id_prescripcion = request.POST['IDpre']
        desc_prescripcion = request.POST['DESCpre'] 

        prescripcion = PRESCRIPCION.objects.get(id_prescripcion=id_prescripcion)
        prescripcion.id_prescripcion = id_prescripcion
        prescripcion.desc_prescripcion = desc_prescripcion
        prescripcion.save()  

        return redirect('listprescripciones')

#ELIMINAR
def form_del_prescripcion(request, id):
    prescripcion = PRESCRIPCION.objects.get(id_prescripcion=id)
    prescripcion.delete()

    return redirect(to='listprescripciones')

#LIST
def listprescripciones(request):
    prescripcion = PRESCRIPCION.objects.all
    datos = {
        'prescripcion': prescripcion
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
        return redirect('listpacientes')

def form_mod_pac(request,id):
    if request.method == 'GET':
        modPAC = PACIENTE.objects.get(rut_pac=id)
        return render(request, "Forms/form_mod_paciente.html", {"PACIENTE": modPAC})
    if request.method == 'POST':
        rut_pac	= request.POST['RUT']
        nombre_pac = request.POST['NOMpac'] 
        correo_pac = request.POST['EMAIL'] 
        numero_pac	= request.POST['NUM'] 
        paciente = PACIENTE.objects.get(rut_pac=rut_pac)
        paciente.rut_pac = rut_pac
        paciente.nombre_pac = nombre_pac
        paciente.correo_pac = correo_pac
        paciente.numero_pac = numero_pac
        paciente.save()  

        return redirect('listpacientes')

#ELIMINAR
def form_del_paciente(request, id):
    paciente = PACIENTE.objects.get(rut_pac=id)
    paciente.delete()

    return redirect(to='listpacientes')


#LIST
def listpacientes(request):
    paciente = PACIENTE.objects.all
    datos = {
        'paciente': paciente
    }
    return render(request,'CesfamWeb/listpacientes.html',datos)

#--De prueba-- Si se consigue base de dato
#def listpacientes(request):
#    paciente = PRESCRIPCION.objects.objects.raw('SELECT * FROM (MODELO) order by id')
#    datos = {
#        'contacto': paciente
#    }
#    return render(request,'CesfamWeb/listpacientes.html',datos)
    
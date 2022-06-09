from django.urls import path
from django.urls.conf import include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('',home,name="home"),
  #Medicamentos
  path('form_medicamento',form_medicamento,name="form_medicamento"),
  path('form_mod_medicamento/<id>',form_mod_medicamento,name="form_mod_medicamento"),
  path('form_del_medicamento/<id>',form_del_medicamento,name="form_del_medicamento"),
  #path('agregar-medicamento',form_med,name="form_medicamento"), <-- Probar por si acaso
  #path('modificar-medicamento/<id>',form_mod_med,name="form_mod_medicamento"), <-- Probar por si acaso
  #path('eliminar-medicamento/<id>',form_del_medicamento,name="form_del_medicamento"),
  path('listmedicamentos',listmedicamentos,name="listmedicamentos"),
  path('reserva',reserva,name="reserva"),
  #Prescripcion
  path('form_pre',form_pre,name="form_pre"),
  path('form_mod_pre/<id>',form_mod_pre,name="form_mod_pre"),
  path('form_del_prescripcion/<id>',form_del_prescripcion,name="form_del_prescripcion"),
  #path('agregar-prescripcion',form_pre,name="form_prescripcion"), <-- Probar por si acaso
  #path('modificar-prescripcion/<id>',form_mod_pre,name="form_mod_prescripcion"), <-- Probar por si acaso
  #path('eliminar-prescripcion/<id>',form_del_prescripcion,name="form_del_prescripcion"),
  path('listprescripciones',listprescripciones,name="listprescripciones"),
  #Paciente
  path('form_paciente',form_paciente,name="form_paciente"),
  path('form_mod_pac/<id>',form_mod_pac,name="form_mod_pac"),
  path('form_del_paciente/<id>',form_del_paciente,name="form_del_paciente"),
  #path('agregar-paciente',form_pac,name="form_paciente"), <-- Probar por si acaso
  #path('modificar-paciente/<id>',form_mod_pac,name="form_mod_paciente"), <-- Probar por si acaso
  #path('eliminar-paciente/<id>',form_del_paciente,name="form_del_paciente"),
  path('listpacientes',listpacientes,name="listpacientes"),
  path('notificarPac/<rut_pac>',notificarPac,name="notificarPac"),
  path('twiliowsp/<rut_pac>',twiliowsp,name="twiliowsp"),
  #Loguear y Desloguear
  path('login/', LoginView.as_view(template_name='RegistroLogin/login.html'),name="login"),
  path('logout/', LogoutView.as_view(template_name='RegistroLogin/logout.html'),name="logout"),
]
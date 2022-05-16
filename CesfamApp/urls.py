from django.urls import path
from django.urls.conf import include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('',home,name="home"),
  #Medicamentos
  path('listmedicamentos',listmedicamentos,name="listmedicamentos"),
  path('reserva',reserva,name="reserva"),
  #Loguear y Desloguear
  path('login/', LoginView.as_view(template_name='RegistroLogin/login.html'),name="login"),
  path('logout/', LogoutView.as_view(template_name='RegistroLogin/logout.html'),name="logout"),
]
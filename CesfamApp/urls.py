from django.urls import path
from django.urls.conf import include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('',home,name="home"),
  path('hospitales',hospitales,name="hospitales"),
  path('contacto',contacto,name="contacto"),
  path('equipo',equipo,name="equipo"),
  path('mision',mision,name="mision"),
  path('valores',valores,name="valores"),
  path('vision',vision,name="vision"),
  #path('login',login,name="login"),
  path('registro',registro,name="registro"),
  path('login/', LoginView.as_view(template_name='RegistroLogin/login.html'),name="login"),
  path('logout/', LogoutView.as_view(template_name='RegistroLogin/logout.html'),name="logout"),
]
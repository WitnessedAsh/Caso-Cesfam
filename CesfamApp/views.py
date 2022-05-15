from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'CesfamWeb/index.html')

def equipo(request):
    return render(request, 'CesfamWeb/conozcanos/equipo.html')

def mision(request):
    return render(request, 'CesfamWeb/conozcanos/mision.html')

def valores(request):
    return render(request, 'CesfamWeb/conozcanos/valores.html')

def vision(request):
    return render(request, 'CesfamWeb/conozcanos/vision.html')

def reserva(request):
    return render(request, 'CesfamWeb/reserva.html')    

#def login(request):
#    return render(request, 'RegistroLogin/login.html')

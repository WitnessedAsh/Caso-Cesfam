from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'CesfamWeb/index.html')

def listmedicamentos(request):
    return render(request, 'CesfamWeb/listmedicamentos.html')

def reserva(request):
    return render(request, 'CesfamWeb/reserva.html')    



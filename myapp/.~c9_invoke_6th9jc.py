from django.shortcuts import render
from dj
# Create your views here.

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

from django.shortcuts import render
from .models import familia
# Create your views here.
def mostrar_familia(request):
    
    padre = familia (nombre ='Marcelo', apellido='Lovato', nacimiento = '1965-12-06', hijos ='2', edad ='56')
    madre = familia (nombre ='Silvina', apellido='Fernandez', nacimiento = '1967-2-25' ,hijos ='2',edad ='52')
    hijo = familia (nombre ='Maximiliano', apellido ='Lovato', nacimiento = '1993-2-26' ,hijos ='0',edad ='29')
    

    return render(request,'familia.html', {'familiar' :[padre, madre , hijo]})
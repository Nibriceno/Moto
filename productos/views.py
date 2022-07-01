from email.mime import message
from pyexpat.errors import messages
from django.shortcuts import render , redirect
from .models import Vehiculo
from .forms import VehiculoForm , customUserCreationForm
from django.contrib.auth import  authenticate , login
from django.contrib import messages
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required , permission_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import render




class VehiculoApiView(APIView):
    serializer_class=vehiculoSerializer
    def get(self,request):
        allVehiculos=Vehiculo.objects.all().values()
        return Response({"Message":"lista de vehiculos", "lista vehiculo":allVehiculos})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=vehiculoSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Vehiculo.objects.create(patente=serializer_obj.data.get("patente"),
                            marca=serializer_obj.data.get("marca"),
                            modelo=serializer_obj.data.get("modelo")
                            )

        Vehiculo=Vehiculo.objects.all().filter(patente=request.data["patente"]).values()
        return Response({"Message":"New Book Added!", "Book":Vehiculo})

class VehiculoViewset(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class =  vehiculoSerializer

# Create your views here.
def home(request):
    return render(request,'productos/index.html')
def contacto(request):
    return render(request,'productos/contacto.html')
def about(request):
    return render(request,'productos/about.html')
def loginvista(request):
    return render(request,'productos/loginvista.html')
def registrarvista(request):
    return render(request,'productos/registrarvista.html')
def servicioMecanico(request):
    return render(request,'productos/ServicioMecanico.html')
def json(request):
    return render(request,'productos/json.html')
def registros(request):
    return render(request,'productos/registros.html')
def logingoogle(request):
    return render(request,'productos/logingoogle.html')
def rest(request):
    return render(request,'productos/rest.html')




     
# Create your views here.
def registros(request):
    lista_vehiculos = Vehiculo.objects.all() #select
    datos = {
        'vehiculos' : lista_vehiculos
    }
    return render(request,'productos/registros.html', datos)

def agregar_vehiculo(request):
    datos = {
        'form' : VehiculoForm()
    }

    if (request.method == 'POST'):
        formulario = VehiculoForm(request.POST , request.FILES  )
        
        if formulario.is_valid():
            formulario.save() #insert
            datos['mensaje'] = "Se guardó vehículo"
        else:
            datos['mensaje'] = "Revise datos"
    return render(request,'productos/agregar_vehiculo.html', datos)

@permission_required('productos.change_productos')
def modificar_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente = id) #select * from Vehiculo where patente = id
    datos = {
        'form' : VehiculoForm(instance = vehiculo)
    }
    if (request.method == 'POST'):
        formulario = VehiculoForm(data = request.POST  , instance = vehiculo)
        if formulario.is_valid():
            formulario.save() #update
            datos['mensaje'] = "Se modificó vehículo"
        else:
            datos['mensaje'] = "Revise datos, no se modificó"
    return render(request,'productos/modificar_vehiculo.html', datos)

@permission_required('productos.delete_productos')
def eliminar_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente = id)
    vehiculo.delete() #delete from Vehiculo where patente = id
    
    return redirect(to='registros')

def registro (request):
    data ={
        'form': customUserCreationForm()       
    }
    if request.method == 'POST':
        formulario = customUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request , "te has registrado correctamente")         
            return redirect (to="home")
        data["form"] = formulario 
        
        
    return render (request , 'registration/registro.html' ,data)

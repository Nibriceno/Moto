from django.urls import path , include
from .views import home , contacto , about , loginvista , servicioMecanico , registrarvista , json , agregar_vehiculo , registros , modificar_vehiculo , eliminar_vehiculo  , logingoogle , registro ,rest,VehiculoViewset 
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Vehiculo' , VehiculoViewset)

urlpatterns = [
    path('',home,name="home"),
    path('contacto/',contacto,name="contacto"),
    path('about/',about,name="about"),
    path('loginvista/',loginvista,name="loginvista"),
    path('servmecanico/',servicioMecanico,name="servicioMecanico"),
    path('regvista/',registrarvista,name="registrarvista"),
    path('json/',json,name="json"),
    path('agregar_vehiculo',agregar_vehiculo,name="agregar_vehiculo"),
    path('registros/',registros,name="registros"),
    path('modificar_vehiculo/<id>',modificar_vehiculo,name="modificar_vehiculo"),
    path('eliminar_vehiculo/<id>',eliminar_vehiculo,name="eliminar_vehiculo"),
    path('logingoogle',logingoogle,name="logingoogle"),
    path('registro',registro,name="registro"),
    path('api/',include(router.urls)),
    path('rest',rest,name="rest"),

   
    
    
   
]




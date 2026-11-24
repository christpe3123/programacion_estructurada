
from django.urls import path
from.import views




urlpatterns = [
    path('', views.Horarios_create, name='horarios_create'),
    path('prueba/',views.datos_de_viaje_pruba, name='datos_de_viaje_pruba'),
    
]

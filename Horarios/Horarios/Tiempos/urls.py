
from django.urls import path
from.import views




urlpatterns = [
    path('', views.Horarios_create, name='horarios_create')
]

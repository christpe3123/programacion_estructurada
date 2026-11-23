from django.contrib import admin
from .models import Aula, BloqueHorario, Curso, Docente, Horario

admin.site.register([Aula, BloqueHorario, Curso, Docente, Horario])

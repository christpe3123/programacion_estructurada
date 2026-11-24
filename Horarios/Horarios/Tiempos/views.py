from django.http import JsonResponse, request
from django.shortcuts import render

from .models import BloqueHorario, Horario


def Horarios_create(request):
    dias = BloqueHorario.DIAS_SEMANA
    horarios = Horario.objects.select_related(
        "curso",
        "docente",
        "aula",
        "bloque",
    )

    bloques = {}
    for horario in horarios:
        intervalo = (horario.bloque.hora_inicio, horario.bloque.hora_fin)
        por_dia = bloques.setdefault(intervalo, {})
        por_dia.setdefault(horario.bloque.dia_semana, []).append(horario)

    filas = [
        {
            "hora_inicio": inicio,
            "hora_fin": fin,
            "celdas": [
                bloques[(inicio, fin)].get(codigo, [])
                for codigo, _ in dias
            ],
        }
        for inicio, fin in sorted(bloques)
    ]

    return render(
        request,
        "index.html",
        {"dias": dias, "filas": filas, "colspan": len(dias) + 1},
    )
    
def datos_de_viaje_pruba(json_data):
    print(json_data)
    
    return JsonResponse({"message": "Datos recibidos correctamente."})
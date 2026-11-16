## 1. Contexto

#La **Universidad de la Vida** necesita organizar las clases de un semestre. Se cuenta con:

#- **10 docentes**.
#- **13 cursos** distribuidos en **4 grupos** de estudiantes.
#- **3 aulas** disponibles.
#- Clases de **lunes a viernes**, en el horario de **08:00 a 12:00**.

#Cada curso tiene una cantidad de horas semanales y debe dictarse en bloques de **1 hora** o **2 horas**.
#Algunos cursos comparten docentes y otros comparten grupos de estudiantes, por lo que es fácil que aparezcan **cruces** 
# (dos clases al mismo tiempo) y **puentes** (horas libres entre clases). El objetivo es construir un horario **válido**, **compacto** y que respete,
# en lo posible, las preferencias de los docentes.
##
## 1.1  El grafo de conflictos, explicado
##
## Un grafo son puntos unidos por líneas. Aquí:
##
##    ●  NODO   = un curso.
##    ──  ARISTA = una línea entre dos cursos que NO pueden
##                 dictarse a la misma hora.
##
## Solo hay línea entre dos cursos cuando comparten algo:
##
##    1) el mismo DOCENTE
##       Ejemplo: C01 y C02, porque las dicta Ana Torres.
##
##    2) el mismo GRUPO de estudiantes
##       Ejemplo: C01 y C03, porque ambos son del grupo G1.
##
## Si no comparten docente ni grupo, NO hay línea:
##
##    C01 ●────────● C03     hay línea   → NO pueden coincidir
##    C01 ●        ● C08     no hay línea → no choca por docente ni grupo
##
## Para que el dibujo no sea una maraña:
##    · las 4 cajas son UN SOLO grafo (no son 4 grafos separados);
##    · cada caja es un GRUPO;
##    · dentro de una caja TODOS los cursos chocan entre sí
##      (por eso no dibujo las líneas internas una por una);
##    · además hay 3 líneas entre cajas distintas (mismo docente);
##      están dibujadas en la lista de abajo.
##
## MAPA DEL GRAFO
##
##    ┌───────────────────────┐        ┌───────────────────────┐
##    │ GRUPO G1 · 5 cursos   │        │ GRUPO G2 · 4 cursos   │
##    │ ● C01  ● C03  ● C05   │        │ ● C02  ● C04          │
##    │ ● C07  ● C09          │        │ ● C08  ● C13          │
##    │ todos chocan entre sí │        │ todos chocan entre sí │
##    │ 10 pares que chocan   │        │ 6 pares que chocan    │
##    └───────────────────────┘        └───────────────────────┘
##    ┌───────────────────────┐        ┌───────────────────────┐
##    │ GRUPO G3 · 3 cursos   │        │ GRUPO G4 · 1 curso    │
##    │ ● C06  ● C10  ● C11   │        │ ● C12                 │
##    │                       │        │                       │
##    │ todos chocan entre sí │        │ isla: sin aristas     │
##    │ 3 pares que chocan    │        │ 0 pares que chocan    │
##    └───────────────────────┘        └───────────────────────┘
##
## LAS 3 LÍNEAS QUE UNEN CAJAS (porque comparten docente)
##
##    C01 (G1) ●──────────● C02 (G2)      Ana Torres
##    C03 (G1) ●──────────● C04 (G2)      Luis Ramírez
##    C09 (G1) ●──────────● C10 (G3)      Rosa Vargas
##
## EJEMPLO: las líneas de C01 (así se lee un nodo)
##
##                        C02 (Ana)
##                            │
##                            │
##                            │
##                            │
##      C05 (G1) ─────────────● C01 ──────── C03 (G1)
##                            │
##                            │
##                    ┌───────┬───────┐
##                    │               │
##                C07 (G1)        C09 (G1)
##
##    C01 está en G1            → choca con C03, C05, C07 y C09
##    C01 lo dicta Ana Torres   → choca con C02
##
##    C01 tiene 5 conflictos:     C02, C03, C05, C07 y C09
##
## RESUMEN
##    · 13 nodos (los 13 cursos).
##    · 22 aristas:
##        19 por grupo   (G1: 10,  G2: 6,  G3: 3)
##         3 por docente (C01-C02, C03-C04, C09-C10)
##    · 1 isla: C12, un nodo sin ninguna línea.
##
## ¿Y EL COLOR?
##    Hay 20 franjas (5 días × 4 horas). Cada franja es un color.
##    Dos cursos unidos por una línea deben tener colores distintos.
##    Si no hay línea, podrían compartir color (si el aula lo permite).
##    Colorear el grafo es, justamente, armar el horario sin cruces.
##
## OJO: C12 no tiene conflictos de docente ni de grupo, pero igual
## necesita un aula. El aula se asigna en una segunda etapa.
##
## =====================================================================
## 2. ALGORITMO Y HORARIO
## =====================================================================
##
##   Modelo del grafo:
##      · Nodo   = bloque de clase (1 h o 2 h).
##      · Arista = dos bloques que comparten docente o grupo.
##      · Color  = franja horaria (20 franjas).
##      · Aula   = segunda etapa (capacidad y disponibilidad).
##
##   Algoritmo:
##      · Backtracking con MRV: en cada paso se elige el bloque con
##        menos franjas válidas.
##      · Los bloques de 2 h solo se prueban en franjas consecutivas.
##      · Se prohíbe una franja si el docente o el grupo ya tienen clase.
##      · Máximo 3 clases simultáneas (3 aulas).
##      · Al final se asignan aulas y se valida el horario completo.
##
##   Para ejecutar:  python evaluacion1.py
##

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
HORAS = ["08:00", "09:00", "10:00", "11:00", "12:00"]

GRUPOS = {"G1": 35, "G2": 28, "G3": 20, "G4": 15}

AULAS = [("A101", 40), ("A102", 35), ("A103", 30)]

PREFERENCIA = {
    "Ana Torres": "tarde",
    "Luis Ramírez": "temprano",
    "Carla Mendoza": "tarde",
    "José Paredes": "flexible",
    "María Quispe": "tarde",
    "Pedro Salas": "temprano",
    "Rosa Vargas": "flexible",
    "Diego Flores": "tarde",
    "Elena Rojas": "flexible",
    "Marco Díaz": "tarde",
}

CURSOS = [
    ("C01", "Álgebra", "Ana Torres", "G1", 4, [2, 2]),
    ("C02", "Cálculo", "Ana Torres", "G2", 2, [2]),
    ("C03", "Programación I", "Luis Ramírez", "G1", 4, [2, 2]),
    ("C04", "Programación II", "Luis Ramírez", "G2", 4, [2, 2]),
    ("C05", "Física I", "Carla Mendoza", "G1", 2, [2]),
    ("C06", "Historia", "José Paredes", "G3", 2, [1, 1]),
    ("C07", "Química", "María Quispe", "G1", 3, [2, 1]),
    ("C08", "Redes", "Pedro Salas", "G2", 4, [2, 2]),
    ("C09", "Inglés I", "Rosa Vargas", "G1", 2, [1, 1]),
    ("C10", "Inglés II", "Rosa Vargas", "G3", 2, [1, 1]),
    ("C11", "Estadística", "Diego Flores", "G3", 2, [2]),
    ("C12", "Biología", "Elena Rojas", "G4", 2, [2]),
    ("C13", "Base de Datos", "Marco Díaz", "G2", 4, [2, 2]),
]

# Cada curso se convierte en uno o más bloques de clase.
BLOQUES = []
for cod, nom, doc, gru, horas, duraciones in CURSOS:
    assert sum(duraciones) == horas
    for i, dur in enumerate(duraciones, 1):
        BLOQUES.append({
            "id": len(BLOQUES),
            "cod": cod,
            "nom": nom,
            "doc": doc,
            "gru": gru,
            "dur": dur,
            "sesion": i,
        })

# Se atacan primero los bloques más difíciles: 2 h y docentes/grupos cargados.
CARGA_DOC = {}
CARGA_GRU = {}
for b in BLOQUES:
    CARGA_DOC[b["doc"]] = CARGA_DOC.get(b["doc"], 0) + b["dur"]
    CARGA_GRU[b["gru"]] = CARGA_GRU.get(b["gru"], 0) + b["dur"]
BLOQUES_ORDEN = sorted(
    BLOQUES,
    key=lambda b: (-b["dur"], -CARGA_DOC[b["doc"]], -CARGA_GRU[b["gru"]], b["cod"])
)


def resolver_horario():
    """Backtracking con MRV sobre las 20 franjas (colores)."""
    docente_ocupado = {d: set() for d in PREFERENCIA}
    grupo_ocupado = {g: set() for g in GRUPOS}
    carga_franja = [0] * 20
    asignados = []
    nodos = [0]

    def opciones(b):
        # Devuelve las (día, hora, franjas) donde el bloque cabe sin cruce.
        dur = b["dur"]
        res = []
        for dia in range(5):
            for h in range(5 - dur):
                slots = [dia * 4 + h + k for k in range(dur)]
                if any(carga_franja[s] >= 3 for s in slots):
                    continue
                if any(s in docente_ocupado[b["doc"]] for s in slots):
                    continue
                if any(s in grupo_ocupado[b["gru"]] for s in slots):
                    continue
                res.append((dia, h, slots))
        return res

    def huecos(campo, clave, dia, extra):
        # Huecos que quedarían para un docente o grupo si se coloca el bloque.
        horas = set()
        for x in asignados:
            if x[campo] == clave and x["dia"] == dia:
                horas.update(s % 4 for s in x["slots"])
        horas.update(s % 4 for s in extra)
        if not horas:
            return 0
        return (max(horas) - min(horas) + 1) - len(horas)

    def costo(b, cand):
        # Preferencias docentes, reparto del curso y evitar puentes.
        dia, h, slots = cand
        p = 0
        p += (huecos("docente", b["doc"], dia, slots)
              + huecos("grupo", b["gru"], dia, slots)) * 4
        pref = PREFERENCIA[b["doc"]]
        if pref == "tarde":
            if b["dur"] == 2:
                if h != 2:
                    p += 8
            elif h < 2:
                p += (2 - h) * 5
        elif pref == "temprano":
            fin = h + b["dur"]
            if fin > 2:
                p += (fin - 2) * 5
        for x in asignados:
            if x["curso"] == b["cod"] and x["dia"] == dia:
                p += 8
        p += sum(1 for x in asignados if x["grupo"] == b["gru"] and x["dia"] == dia)
        return p

    def rec(pendientes):
        nodos[0] += 1
        if not pendientes:
            return True

        # MRV: se elige el bloque con menos opciones válidas.
        mejor = None
        for b in pendientes:
            ops = opciones(b)
            if not ops:
                return False
            if mejor is None or len(ops) < len(mejor[1]):
                mejor = (b, ops)

        b, ops = mejor
        ops.sort(key=lambda c: costo(b, c))
        idx = pendientes.index(b)
        resto = pendientes[:idx] + pendientes[idx + 1:]

        for dia, h, slots in ops:
            for s in slots:
                carga_franja[s] += 1
                docente_ocupado[b["doc"]].add(s)
                grupo_ocupado[b["gru"]].add(s)
            asignados.append({
                "id": b["id"], "curso": b["cod"], "nombre": b["nom"],
                "docente": b["doc"], "grupo": b["gru"], "dur": b["dur"],
                "dia": dia, "hora": h, "slots": slots, "aula": None,
            })
            if rec(resto):
                return True
            asignados.pop()
            for s in slots:
                carga_franja[s] -= 1
                docente_ocupado[b["doc"]].discard(s)
                grupo_ocupado[b["gru"]].discard(s)
        return False

    if not rec(BLOQUES_ORDEN):
        return None, nodos[0]
    return asignados, nodos[0]


def asignar_aulas(horario):
    """Segunda etapa: aula con capacidad suficiente y libre en esas franjas."""
    ocupacion = {s: {} for s in range(20)}
    orden = sorted(horario, key=lambda x: -GRUPOS[x["grupo"]])

    def rec(i):
        if i == len(orden):
            return True
        b = orden[i]
        for nombre, cap in sorted(AULAS, key=lambda r: r[1]):
            if cap < GRUPOS[b["grupo"]]:
                continue
            if all(nombre not in ocupacion[s] for s in b["slots"]):
                for s in b["slots"]:
                    ocupacion[s][nombre] = b["id"]
                b["aula"] = nombre
                if rec(i + 1):
                    return True
                for s in b["slots"]:
                    del ocupacion[s][nombre]
                b["aula"] = None
        return False

    return rec(0)


def validar(horario):
    """Revisa todas las restricciones duras y devuelve la lista de errores."""
    errores = []

    # 1) Horas y número de bloques por curso.
    for cod, nom, doc, gru, horas, duraciones in CURSOS:
        suma = sum(x["dur"] for x in horario if x["curso"] == cod)
        if suma != horas:
            errores.append(f"{cod}: {suma} h asignadas, se esperaban {horas} h")
        if len([x for x in horario if x["curso"] == cod]) != len(duraciones):
            errores.append(f"{cod}: número de bloques incorrecto")

    # 2) Cruces: en cada franja no puede repetirse docente, grupo ni aula.
    for campo, nombre in (("docente", "docente"), ("grupo", "grupo"), ("aula", "aula")):
        for s in range(20):
            vistos = {}
            for x in horario:
                if s in x["slots"]:
                    clave = x[campo]
                    if clave in vistos:
                        errores.append(
                            f"Cruce de {nombre} en {DIAS[s // 4]} {HORAS[s % 4]}: "
                            f"{vistos[clave]} y {x['curso']}"
                        )
                    vistos[clave] = x["curso"]

    # 3) Capacidad del aula.
    for x in horario:
        cap = dict(AULAS).get(x["aula"], 0)
        if cap < GRUPOS[x["grupo"]]:
            errores.append(
                f"{x['curso']} en {x['aula']}: capacidad {cap} < {GRUPOS[x['grupo']]}"
            )

    # 4) Los bloques de 2 h deben ocupar dos franjas consecutivas.
    for x in horario:
        if x["dur"] == 2:
            esperado = [x["dia"] * 4 + x["hora"], x["dia"] * 4 + x["hora"] + 1]
            if x["slots"] != esperado or x["hora"] > 2:
                errores.append(f"{x['curso']}: bloque de 2 h mal ubicado")

    return errores


def pref_ok(x):
    """Indica si la sesión cumple la preferencia horaria del docente."""
    pref = PREFERENCIA[x["docente"]]
    if pref == "flexible":
        return True
    if pref == "tarde":
        return x["hora"] >= 2
    fin = x["hora"] + x["dur"]
    return fin <= 2


def puentes(horario, campo):
    """Cuenta horas libres entre la primera y la última clase del día."""
    total = 0
    detalle = {}
    for clave in sorted({x[campo] for x in horario}):
        sub = 0
        for dia in range(5):
            horas = set()
            for x in horario:
                if x[campo] == clave and x["dia"] == dia:
                    horas.update(s % 4 for s in x["slots"])
            if horas:
                sub += (max(horas) - min(horas) + 1) - len(horas)
        detalle[clave] = sub
        total += sub
    return total, detalle


def formato_hora(h, dur):
    return f"{HORAS[h]}-{HORAS[h + dur]}"


def main():
    print("=" * 78)
    print("HORARIO · UNIVERSIDAD DE LA VIDA")
    print("=" * 78)

    horario, nodos = resolver_horario()
    if horario is None:
        print("No se encontró un horario válido.")
        return

    if not asignar_aulas(horario):
        print("No se pudieron asignar aulas.")
        return

    errores = validar(horario)

    horario.sort(key=lambda x: (x["dia"], x["hora"], x["aula"]))
    print("\n1) HORARIO PROPUESTO\n")
    print(f"{'Día':<10}{'Hora':<14}{'Curso':<7}{'Nombre':<18}{'Docente':<16}{'Grupo':<7}{'Aula':<6}")
    print("-" * 78)
    for x in horario:
        print(
            f"{DIAS[x['dia']]:<10}{formato_hora(x['hora'], x['dur']):<14}"
            f"{x['curso']:<7}{x['nombre']:<18}{x['docente']:<16}"
            f"{x['grupo']:<7}{x['aula']:<6}"
        )

    print("\n2) VALIDACIÓN DE RESTRICCIONES DURAS\n")
    if errores:
        for e in errores:
            print("  [X]", e)
    else:
        print("  [OK] Sin cruces de docente")
        print("  [OK] Sin cruces de grupo")
        print("  [OK] Sin cruces de aula")
        print("  [OK] Capacidad de aulas respetada")
        print("  [OK] Todas las horas semanales asignadas")
        print("  [OK] Bloques de 2 h consecutivos dentro del horario")

    total = len(horario)
    ok = sum(1 for x in horario if pref_ok(x))
    pf, df = puentes(horario, "docente")
    pg, dg = puentes(horario, "grupo")
    franjas = len({s for x in horario for s in x["slots"]})

    print("\n3) MÉTRICAS DE CALIDAD\n")
    print(f"  Sesiones programadas : {total}")
    print(f"  Franjas utilizadas   : {franjas} de 20")
    print(f"  Preferencias docentes: {ok}/{total} ({100 * ok / total:.0f}%)")
    print(f"  Puentes de docentes  : {pf}")
    print(f"  Puentes de grupos    : {pg}")
    if df:
        print("    Docentes:", ", ".join(f"{k}={v}" for k, v in df.items() if v))
    if dg:
        print("    Grupos  :", ", ".join(f"{k}={v}" for k, v in dg.items() if v))
    uso = {}
    for x in horario:
        uso[x["aula"]] = uso.get(x["aula"], 0) + x["dur"]
    print("  Uso de aulas (horas) :", ", ".join(f"{k}={v}" for k, v in sorted(uso.items())))
    print(f"  Nodos explorados     : {nodos}")

    print("\n4) VISTA POR DÍA Y HORA (códigos de curso)\n")
    print("  Un curso de 2 h aparece en las dos horas que ocupa.\n")
    cab = f"{'Hora':<10}" + "".join(f"{d:<15}" for d in DIAS)
    print(cab)
    print("-" * len(cab))
    for h in range(4):
        fila = f"{HORAS[h]:<10}"
        for dia in range(5):
            slot = dia * 4 + h
            clases = [x for x in horario if slot in x["slots"]]
            txt = " ".join(x["curso"] for x in clases)
            fila += f"{txt:<15}"
        print(fila)
    print()


if __name__ == "__main__":
    main()

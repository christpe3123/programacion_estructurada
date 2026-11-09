from collections import defaultdict, deque


def orden_tareas(tareas, dependencias):
    grafo, grado = defaultdict(list), {t: 0 for t in tareas}
    for antes, despues in dependencias:
        grafo[antes].append(despues)
        grado[despues] += 1
    cola = deque([t for t in tareas if grado[t] == 0])
    orden = []
    while cola:
        t = cola.popleft()
        orden.append(t)
        for sig in grafo[t]:
            grado[sig] -= 1
            if grado[sig] == 0:
                cola.append(sig)
    return orden if len(orden) == len(tareas) else "Ciclo detectado"

print(orden_tareas(['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D')]))  
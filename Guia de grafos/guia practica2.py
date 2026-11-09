import heapq


def ruta_mas_corta(grafo, inicio, fin):
    dist = {n: float('inf') for n in grafo}
    dist[inicio], prev, cola = 0, {}, [(0, inicio)]

    while cola:
        d, u = heapq.heappop(cola)
        if u == fin:
            break
        if d > dist[u]:
            continue
        for v, peso in grafo[u]:
            nd = d + peso
            if nd < dist[v]:
                dist[v], prev[v] = nd, u
                heapq.heappush(cola, (nd, v))

    camino, actual = [], fin
    while actual in prev:
        camino.append(actual)
        actual = prev[actual]

    if actual == inicio:
        camino.append(inicio)
        return list(reversed(camino)), dist[fin]

    return [], float('inf')





print(ruta_mas_corta({
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}, 'A', 'D'))
from collections import deque
def red_conectada(grafo, inicio):
    visitados = {inicio}
    cola = deque([inicio])
    while cola:
        u = cola.popleft()
        for v in grafo[u]:
            if v not in visitados:
                visitados.add(v); cola.append(v)
    return len(visitados) == len(grafo)
print(red_conectada({
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}, 'A'))
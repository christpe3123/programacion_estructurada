def hay_ciclo(grafo):
    estado = {}

    def dfs(u):
        estado[u] = 1
        for v in grafo.get(u, []):
            if estado.get(v, 0) == 1:
                return True
            if estado.get(v, 0) == 0 and dfs(v):
                return True
        estado[u] = 2
        return False

    return any(dfs(n) for n in grafo if estado.get(n, 0) == 0)

print(hay_ciclo({
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}))
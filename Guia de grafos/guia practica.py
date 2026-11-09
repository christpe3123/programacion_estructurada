from collections import deque


def sugerir_amigos(grafo, usuario):
    amigos = set(grafo[usuario])
    sugerencias = {}
    for amigo in amigos:
        for ada in grafo[amigo]:
            if ada != usuario and ada not in amigos:
                sugerencias[ada] = sugerencias.get(ada, 0) + 1
    return sorted(sugerencias, key=sugerencias.get, reverse=True)


grafo = {
    'ana': ['luis', 'pedro'],
    'luis': ['ana', 'pedro', 'maria'],
    'pedro': ['ana', 'luis'],
    'maria': ['luis', 'juan'],
    'juan': ['maria'],
}

print(sugerir_amigos(grafo, 'ana'))  # ['maria', 'juan']

def cargar_datos():
    lista = [2,5,6,8,10]
    return lista

#filtrador de condicionales
def filtrar_elementos(lista):
    lista_filtrada = []
    for elemento in lista:
        if elemento >= 0:
            lista_filtrada.append(elemento)
    return lista_filtrada




#funcion de recorrido e iteracion(bucle)


def procesar_calculos(lista):
    if not lista:
        print("/n[Aviso]: lista esta vacia.")
        return 0.0
    
    acumulador = 0.0
    for elemento in lista:
        acumulador += elemento

    promedio = acumulador / len(lista)
    
    print("/n--- PROCESAMIENTO y Calculos ---")
    print(f"Suma total acumulada: {acumulador}")
    print(f"promedio de los datos: {promedio:.2f}")
    return promedio

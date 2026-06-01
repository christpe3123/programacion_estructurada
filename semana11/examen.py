# 1.1 Función de Carga y Flujo Secuencial
def cargar_datos():
    lista = [1, 2, 3, 4, 5]
    return lista
def flujo_secuencial():
    datos = cargar_datos()
    print("Datos cargados:", datos)

# 1.2 Función de Carga y Flujo Condicional
def cargar_datos_condicional():
    lista = [1, 2, 3, 4, 5]
    return lista
def flujo_condicional():
    datos = cargar_datos_condicional()
    if len(datos) > 3:
        print("La lista tiene más de 3 elementos.")
    else:
        print("La lista tiene 3 o menos elementos.")

# 1.3 Función de Carga y Flujo Iterativo
def cargar_datos_iterativo():
    lista = [1, 2, 3, 4, 5]
    return lista
def flujo_iterativo():
    datos = cargar_datos_iterativo()
    for numero in datos:
        print("Número:", numero)

# Ejecución de las funciones    
if __name__ == "__main__":
    print("Flujo Secuencial:")
    flujo_secuencial()
    
    print("\nFlujo Condicional:")
    flujo_condicional()
    
    print("\nFlujo Iterativo:")
    flujo_iterativo()

#1.4 funcion de ordenamiento de la estructura
def ordenar_datos():
    lista = [5, 3, 1, 4, 2]
    lista_ordenada = sorted(lista)
    return lista_ordenada
def flujo_ordenamiento():
    datos_ordenados = ordenar_datos()
    print("Datos ordenados:", datos_ordenados)
print("\nFlujo de Ordenamiento:")
flujo_ordenamiento()
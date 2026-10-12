#caso 1 almacen de productos - 6 puntos
#Un restaurante debe revisar que productos ncesita comprar, cuanto le falta de cada uno y si dispone del presupuesto para reponerlos.



inventario = [
    {"producto": "Pollo", "kg": 4, "minimo": 8, "precio": 13},
    {"producto": "Arroz", "kg": 7, "minimo": 6, "precio": 5},
    {"producto": "Papa", "kg": 0, "minimo": 5, "precio": 3},
    {"producto": "Limon", "kg": 2, "minimo":5, "precio": 7},
    {"producto": "Harina", "kg": 9, "minimo": 9, "precio": 4},
    {"producto": "Azucar", "kg": 1, "minimo": 4, "precio": 5}
]

presupuesto = 90
#Para los productos agotados o por reponer, calcule los kilogramos faltantes y el costo de reposición
#(faltante × precio por kg).
total_kg_minimo = sum(venta["minimo"] for venta in inventario)
print(f"total de kg minimo: {total_kg_minimo}")

total_kg = sum(venta["kg"] for venta in inventario)
print(f"total de kg: {total_kg}")
calculo = total_kg_minimo - total_kg
print(f"descuento de kg y minimo: {calculo}")

total_precio = sum(venta["precio"] for venta in inventario)
print(total_precio)
resultado = total_precio - calculo
print(f"necesita gastar: {resultado}")
print(f"presupuesto actual: {presupuesto}")
resultado1 = presupuesto - resultado 
print(f"en total le quedaria: {resultado1}")

for inventario in inventario:
    if inventario["kg"] <= 0:
        print(f"{inventario["producto"]} esta agotado {inventario['kg']}")
        print(f"estos producto necesita reponer: {inventario["minimo"]} kg")
    
# Para los productos agotados o por reponer, calcule los kilogramos faltantes y el costo de reposición (faltante × precio por kg).
    if inventario["kg"] < inventario["minimo"]:
        faltante = inventario["minimo"] - inventario["kg"]
        costo_reposicion = faltante * inventario["precio"]
        print(f"faltante de {inventario['producto']}: {faltante} kg, costo de reposición: {costo_reposicion}")

# Calcule el costo total de completar todos los mínimos y la cantidad de productos que necesitan compra.
    if inventario["kg"] < inventario["minimo"]:
        faltante = inventario["minimo"] - inventario["kg"]
        costo_reposicion = faltante * inventario["precio"]
        print(f"faltante de {inventario['producto']}: {faltante} kg, costo de reposición: {costo_reposicion}")



#Compare el costo total con el presupuesto y muestre cuánto sobra o cuánto falta para comprar todo.
    if inventario["kg"] < inventario["minimo"]:
        faltante = inventario["minimo"] - inventario["kg"]
        costo_reposicion = faltante * inventario["precio"]
        print(f"faltante de {inventario['producto']}: {faltante} kg, costo de reposición: {costo_reposicion}")


# Identifique el producto cuya reposición tiene el costo más alto (muestre el nombre y el costo).
    if inventario["kg"] < inventario["minimo"]:
        faltante = inventario["minimo"] - inventario["kg"]
        costo_reposicion = faltante * inventario["precio"]
        print(f"faltante de {inventario['producto']}: {faltante} kg, costo de reposición: {costo_reposicion}")
ventas_hoy = [    
    {"mesa": 1, "total": 150, "metodo": "yape",     "descuento": 10},
    {"mesa": 2, "total": 80,  "metodo": "efectivo", "descuento": 0},
    {"mesa": 3, "total": 220, "metodo": "tarjeta",  "descuento": 20}, 
    {"mesa": 4, "total": 45,  "metodo": "yape",     "descuento": 0},
    {"mesa": 5, "total": 180, "metodo": "efectivo", "descuento": 15},
    {"mesa": 6, "total": 95,  "metodo": "tarjeta",  "descuento": 5},
    {"mesa": 7, "total": 300, "metodo": "yape",     "descuento": 30}
]

#Para cada mesa, calcule el monto cobrado restando el descuento al total original; muestre ambos valores.
for venta in ventas_hoy:
    monto_cobrado = venta["total"] - venta["descuento"]
    print(f"Mesa {venta['mesa']}: total original: {venta['total']}, Descuento: {venta['descuento']}, total con descuento: {monto_cobrado}")


# Calcule el total original, el total de descuentos y el total efectivamente cobrado.

total_original = sum(venta["total"] for venta in ventas_hoy)
total_descuentos = sum(venta["descuento"] for venta in ventas_hoy)
total_cobrado = sum(venta["total"] - venta["descuento"] for venta in ventas_hoy)

print(f"total original: {total_original}")
print(f"total de descuentos:  {total_descuentos}")
print(f"total efectivamente cobrado: {total_cobrado}")


# Acumule el dinero realmente cobrado por Yape, efectivo y tarjeta, e indique cuántas mesas utilizaron cada medio.
dinero_yape = sum(venta["total"] - venta["descuento"] for venta in ventas_hoy if venta["metodo"] == "yape")
mesas_yape = sum(1 for venta in ventas_hoy if venta["metodo"] == "yape")
print(f"dinero cobrado por yape: {dinero_yape}, mesas que usaron yape: {mesas_yape}")


# Identifique la mesa con el mayor monto cobrado después del descuento.
if ventas_hoy:
    mesa_mayor = max(ventas_hoy, key=lambda venta: venta["total"] - venta["descuento"])
    monto_mayor = mesa_mayor["total"] - mesa_mayor["descuento"]
    print(f"la mesa con mayor monto es: {mesa_mayor['mesa']} y con monto {monto_mayor}")


#Muestre solo las mesas cuyo monto cobrado es mayor que S/ 150 y cuente cuántas son.
if ventas_hoy:
    mesas_mayor_150 = [venta for venta in ventas_hoy if venta["total"] - venta["descuento"] > 150]
    print(f"mesas con monto mayor a S/ 150: {[venta['mesa'] for venta in mesas_mayor_150]}")
    print(f"cantidad de mesas con monto mayor a S/ 150: {len(mesas_mayor_150)}")


# Calcule el promedio realmente cobrado por mesa e indique
# si el ingreso total alcanza la meta del día de S/ 1,000; muestre el exceso o faltante.
if ventas_hoy:
    promedio_cobrado = total_cobrado / len(ventas_hoy)
    print(f"promedio realmente cobrado por mesa: {promedio_cobrado}")

    meta_dia = 1000
    if total_cobrado >= meta_dia:
        exceso = total_cobrado - meta_dia
        print(f"si alcanzo la meta del dia,Exceso: {exceso}")
    else:
        faltante = meta_dia - total_cobrado
        print(f"no se alcanzo la meta del dia,Faltante: {faltante}")
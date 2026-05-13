#arreglos de datos 
#arrays
#ejemplo de un arreglo unidimensional

productos = ["Laptop", "Smartphone", "Tablet", "Monitor", "Teclado"]

print(f"El primer producto es: {productos[0]}")
print(f"El ultimo producto es: {productos[-1]}")

productos[1] = "Smartwatch"

productos.append("Mouse")

productos.pop(2)
print("Productos actualizados:", productos)
for i , producto in enumerate(productos):
    print(f"Producto {i + 1}: {producto}")


print(f"\nCantidad de productos: {len(productos)}")
#arreglos de datos 
#arrays
#ejemplo de un arreglo unidimensional
import numpy as np

array=np.array(["Laptop", "Smartphone", "Tablet", "Monitor", "Teclado"])

print(f"El primer producto es: {array[0]}")
print(f"El ultimo producto es: {array[-1]}")

array[1] = "Smartwatch"

print("Productos actualizados:", array)
for i , producto in enumerate(array):
    print(f"Producto {i + 1}: {producto}")


print(f"\nCantidad de productos: {len(array)}")
'''Cree un programa en Python que:
1. Cree una lista con 3 calificaciones decimales y la muestre.
2. Cambie una calificación utilizando su posición.
3. Cree otra lista con 2 calificaciones adicionales y una ambas listas.
4. Ordene las calificaciones con sort().
5. Muestre la nota menor, la mayor y la cantidad total usando min(), max() y len().
6. Solicite una nueva calificación con input() y agréguela con append().
7. Inserte una calificación en la posición 1 usando insert().
8. Elimine una calificación con remove().
9. Verifique con if e in si una nota específica se encuentra en la lista.
10. Muestre la lista final de calificaciones.
Importante: convierta las notas ingresadas por el usuario utilizando float().
''' 
calificaciones = [78.5 , 98.6  , 89.9]
print(calificaciones)
calificaciones.insert(1, 75.5)
print(calificaciones)
calificaciones_adicionales = [88 , 93]
calificaciones = calificaciones + calificaciones_adicionales
calificaciones .sort()
print("Lista ordenada" , calificaciones)
print("Nota menor:" , min(calificaciones))
print("Nota mayor:" , max(calificaciones))
print("Cantidad total:", len(calificaciones))
nueva_nota = float(input("Ingrese una nueva calificación: " ))
calificaciones.insert(1 , 75.5)
calificaciones.remove(89.9)
nota_a_buscar = 88
if nota_a_buscar in calificaciones:
    print(f"La nota {nota_a_buscar} sí se encuentra en la lista.")
print("Lista final de calificaciones: " , calificaciones)
                   














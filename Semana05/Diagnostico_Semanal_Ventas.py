"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""
#Autor. Karla Cerdas Chaves

dias= ["Lunes" , "Martes" , "Miercoles" , "Jueves", "Viernes"]
ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 64000
meta_norte = 70000

# TODO: calcula total, cantidad, mayor y menor para Centro.
total_centro = sum ( ventas_centro) #total de ventas semanal
cantidad_centro = len(ventas_centro) #Cantidad de dias registrados

promedio_centro = total_centro / cantidad_centro #promedio ventas diario
menor_centro = min(ventas_centro) # Venta minima de la tienda del centro
mayor_centro = max(ventas_centro) #vetan maxima de la tienda del centro
dia_mayor = dias [ventas_centro.index(mayor_centro)]
porcentaje_centro = total_centro * 100 / meta_centro
print(total_centro)
print(porcentaje_centro)
print(dia_mayor , mayor_centro)

# TODO reoite los indicadores para Norte.
total_norte = sum ( ventas_norte) #total de ventas semanal
cantidad_norte = len(ventas_norte) #Cantidad de dias registrados

promedio_norte = total_norte / cantidad_norte #promedio ventas diario
menor_norte = min(ventas_norte) # Venta minima de la tienda del centro
mayor_norte = max(ventas_norte) #vetan maxima de la tienda del centro
dia_mayor = dias [ventas_norte.index(mayor_norte)]
porcentaje_norte = total_norte* 100 / meta_norte
print(total_norte)
print(porcentaje_norte)

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.
if total_centro > meta_centro:
    estado_centro = "meta superada"
if total_centro == meta_centro:
    estado_centro = "meta alcanzada exactamente"
else:
    estado_centro = "meta NO alcanzada"
    
if total_norte > meta_norte:
    estado_norte = "meta superada"
elif total_norte == meta_norte:
    estado_norte = "meta alcanzada exactamente"
else:
    estado_norte = "meta NO alcanzada"
# TODO: compara los totales y los rangos.
if total_centro > total_norte:
    tienda_mayor_ventas = "Tienda del Centro"
elif total_norte > total_centro:
    tienda_mayor_ventas = "Tienda del Norte"
else:
    tienda_mayor_venta = "Ambas tiendas tienen el mismo total"

# TODO: presenta un reporte con etiquetas claras y f-strings.
print("COMPARACIÓN SEMANAL DE TIENDAS")
print("-" * 70)
print(f"Centro | total: ₡ {total_centro: ,.2f} | meta ₡  {meta_centro: ,.2f} | cumplimiento % {porcentaje_centro}")
print(f"Centro_logro: {estado_centro}\n")
print(f"Norte | total: ₡ {total_norte ,.2f} | meta ₡  {meta_norte: ,.2f} | cumplimiento % {porcentaje_norte}") 
print (f"Norte logro: {estado_norte}\n")
print("Tienda con mayor ventas: " , tienda_mayor_venta)
# TODO: escribe las tres conclusiones solicitadas en la guía.

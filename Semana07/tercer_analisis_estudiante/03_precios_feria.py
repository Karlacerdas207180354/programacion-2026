"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo 

# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
indice = 0  
mayores_al_promedio = 0
while indice < len(precios):
    if precios[indice] > promedio: 
        mayores_al_promedio += 1
    indice += 1
# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >= 300:
    variacion = "Alta"
elif rango >= 150:
    variacion = "Moderada"
else:
    variacion = "baja"
# TODO: Muestre producto y todos los resultados.
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.
print(f"---Analisis de Precios para: {producto}---")
print(f"Promedio: ₡{promedio}")
print(f"Minimo: ₡{minimo} , Maximo: ₡{maximo}")
print(f"Rango: ₡{rango} , Variación: {variacion}")
print(f"Precios sobre el promedio: {mayores_al_promedio}")

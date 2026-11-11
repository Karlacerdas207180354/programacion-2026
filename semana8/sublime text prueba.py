"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 108, 102, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.
total = sum(consumos_litros)
promedio = total / len(consumos_litros) 
# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[-1]
ahorro = primer_dia - ultimo_dia 
porcentaje = (ahorro / primer_dia) * 100

#       de reducción respecto al primer día.
# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
if porcentaje >= 15:
    clasificacion = "Reducción Alta"
elif porcentaje >0 :
    clasificacion = "Reducción Moderada"
else:
    clasificacion = "Sin Reducción"
# TODO: Muestre los cinco resultados.
print(f"total {total} L; promedio {promedio: .1f} L; ahorro {ahorro} L; reducción {porcentaje: .0f} %;")
print(clasificacion)
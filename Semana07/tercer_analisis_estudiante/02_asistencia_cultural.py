"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300
total_asistencia = 0
cantidad_bloques = 0 
# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
# multiplique 300 que es la capacidad x 0.70 que es el porcentaje me dio 210 debe ser >210 segun la instruccion 
#el promedio lo saque del total_asistencia / cantidad_bloques y el porcentaje es promedio / capacidad se multiplica x 100
for asistencia in asistencias:
    if asistencia > 210:
        total_asistencia += asistencia
        cantidad_bloques += 1
# TODO: Calcule el promedio y su porcentaje de ocupación.
promedio = total_asistencia / cantidad_bloques
porcentaje = (promedio / capacidad) * 100
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if porcentaje >= 80:
    estado = "Ocupación Alta"
elif porcentaje >= 50:
    estado = "Ocupación Media"
else:
    estado = "Ocupación baja"
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
print(f"total {total_asistencia:.0f}, promedio {promedio:.0f}, porcentaje {porcentaje:.0f} %, bloques {cantidad_bloques}, estado {estado }.")
"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).

# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
total_minutos = 0 #suma todos los minutos de atención
conteo_categorias = {"Acceso": 0 , "Equipo": 0 ,"Red": 0} # cuenta cuantos casos hay de cada categoria
casos_urgentes = 0 # cuenta los casos pendientes
caso_mas_largo = ("" , 0) # guarda el ID y los minutos del caso mas largo
provincias_pendientes = set() # Guarda las provincias q tienen casos pendientes
listas_urgentes = [] # Guarda los casos urgentes en forma de tuplas.

# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.
for caso in incidencias:
    id_caso = caso["id"]
    categoria = caso ["categoria"]
    minutos = caso["minutos_atencion"]
    resuelto = caso ["resuelto"]
    provincia = caso ["provincia"]

    total_minutos += minutos
    conteo_categorias [categoria] += 1 


    if not resuelto:
        casos_urgentes += 1
        provincias_pendientes.add(provincia)

        # Identificar casos urgentes de 60 minutos o más
        if minutos >= 60:
            listas_urgentes.append((id_caso, minutos))

    # Identificar el caso con más minutos de atención
    if minutos > caso_mas_largo[1]:
        caso_mas_largo = (id_caso, minutos)
# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.
promedio = total_minutos / len(incidencias)
print("Total de minutos: " , total_minutos)
print("Promedio de minutos: " , promedio)
print("Conteo por categoria: " , conteo_categorias)
print("Cantidad de pendientes: " , casos_urgentes)
print("Provincias pendientes: " , provincias_pendientes)
print("Casos urgentes: " , listas_urgentes)
print("Caso mas largo: " , caso_mas_largo)
print("San Jose tiene pendientes: " , "San Jose" in provincias_pendientes)
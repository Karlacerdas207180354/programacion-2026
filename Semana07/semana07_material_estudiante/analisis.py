from sedes import emprendimientos

print("emprendimientos registrados: " , len(emprendimientos))
print("Primer emprendimiento: " , emprendimientos[0]["nombre"])
print("Primer emprendimiento ventas:" , emprendimientos[0] ["ventas"])

print("\nANALISIS SEMANAL DE EMPRENDEDORES")
provincias = set() #provincias {1,2,3,4}
#Cada vuelta procesara un diccionario
for empre in emprendimientos:
    total = sum(empre["ventas"])
    porcentaje = total / empre ["meta"] * 100
    if porcentaje >= 100:
        estado = "Meta alcanzada"
    elif porcentaje >= 80:
        estado = "Cerca de la meta"
    else:
        estado = "Requiere atención!"

    print(
        f"{empre["nombre"]} | ₡{total:,.2f}"
        f"Cumplimiento: {porcentaje:.2f} % | {estado}"
    )

print("Provincias" , provincias)
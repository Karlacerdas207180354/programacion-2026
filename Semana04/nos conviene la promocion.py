#Nos conviene la promoción ??
#Autor: Karla Cerdas Chaves
producto_cafe = ["Cafe", 5000, 20]



# 1. Selección con índce
producto = producto_cafe [0]
precio_actual = producto_cafe [1]
unidades_actuales = producto_cafe [2]


# 2. Calcular descuento y precio promocional
descuento = precio_actual * 15 / 100
precio_promocional = precio_actual - descuento


# 3. Ingreso actual
ingreso_actual = precio_actual * unidades_actuales

# 4. Proyección de unidades (+20%)
aumento_unidades = unidades_actuales * 20 / 100
unidades_proyectadas = unidades_actuales + aumento_unidades

# 5. Ingreso proyectado con promoción
ingreso_proyectado = precio_promocional * unidades_proyectadas
diferencia = ingreso_proyectado - ingreso_actual

#6. Solucion
if diferencia > 0 :
    recomendamos = "Lanzar"
else:
    
    recomendamos = "No lanzar"
#7.Salidas
print("analisis de promoción")
print(f"resultado del analisis: {recomendamos} la promocion")
print(f"La diferencia de ingresos es de {diferencia}. Decisión: {recomendamos}")
print(f" Ingreso Actual: {ingreso_actual} \ningreso Proyectado: {ingreso_proyectado}\nDiferencia: {diferencia}\nRecomendación:{recomendamos}")

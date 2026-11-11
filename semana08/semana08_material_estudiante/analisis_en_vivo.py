"""Semana 8: la red hospitalaria nos contrata como analistas de datos.

Construimos el informe debajo de este inicio con GUIA_ESTUDIANTE.md.
Leemos la fuente preparada en fuente.py y contamos las menciones recibidas.
"""

from fuente import cargar_datos


USAR_RESPALDO = False  # Lo cambiamos solo si recibimos copias actualizadas.
registros, equivalencias, origen = cargar_datos(USAR_RESPALDO)
print("Fuente:", origen)
print("Registros recibidos:", len(registros))
print("Equivalencias publicadas:", len(equivalencias))

#FASE 1 : COTAR MEDICAMENTOS
conteo_medicamento = {}
conteo_recetas = 0

# Comencemos aquí con la muestra y después construyamos nuestro contador.
print("\nMUESTRA DE DATOS")
for indice in range(3):  # 0  1  2 |3
    registro = registros[indice]
    print(
            f"\nCédula: {registro['paciente_cedula']}\n - Paciente:{registro['paciente_nombre']}"
            f"\n - Diagnóstico:{registro['diagnostico']}\n - Medicamententos: {registro['medicamentos']}\n"
        )    
    #CONTEO
    for medicamento in registro['medicamentos']:
        if medicamento in conteo_medicamento:
            conteo_medicamento[medicamento] += 1
        else:
            conteo_medicamento[medicamento] = 1
        conteo_recetas += 1

print("\n CONTEO DE MEDICAMENTOS")
print("Total de recetas:", conteo_recetas)
print(conteo_medicamento)



#FASE 1 : COTAR MEDICAMENTOS
conteo_medicamento = {}
conteo_recetas = 0
#FASE 2: LIMPIEZA DE DATOS
equivalencias = {
    "acetaminofén": "acetaminofen" , 
    "paracetamol": "acetaminofen",
    "antiácido": "antiacido" , 
    "losartán": "losartan"
}
for registro in registros:
    
    for medicamento in registro['medicamentos']:
        nombre = medicamento.strip().lower() #PARACETAMOL -> "paracetamol"
        #aplicacion fase 2
        if nombre in equivalencias:
            nombre = equivalencias[nombre]
    
        if nombre in conteo_medicamento:
            conteo_medicamento[nombre] += 1
        else:
            conteo_medicamento[nombre] = 1
        conteo_recetas += 1

print("\n-------- CONTEO DE MEDICAMENTOS ---------")
print("Total de recetas:", conteo_recetas)
for medicamento, cantidad in conteo_medicamento.items():
    print(f"- {medicamento}: {cantidad}")

#fase 3 conteo de pacientes por hospitales
conteo_hospital = {}
conteo_enfermedades = {}
for registro in registros:
    hospital = registro["hospital"]
    if hospital not in conteo_hospital:
        conteo_hospital[hospital] = 0 
    conteo_hospital[hospital] += 1
print("\nANTECEDENTES POR HOSPITAL")
for hospital, cantidad in conteo_hospital.items():
    print("-", hospital, ":", cantidad)
#fase 4 contar enfermedades
for registro in registros:
    enfermedad = registro["diagnostico"]
    if enfermedad not in conteo_enfermedades:
        conteo_enfermedades[enfermedad] = 0
    conteo_enfermedades[enfermedad] += 1
print("\nANTECEDENTES POR HOSPITAL: ")
for enfermedad, cantidad in conteo_enfermedades.items():
    print(f"- {enfermedad}: {cantidad}")






#print(type(registro["Medicamentos"]))   
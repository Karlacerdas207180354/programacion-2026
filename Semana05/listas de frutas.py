#Listas
frutas = ["Manzana" , "Pera" , "Uvas"]
print(frutas)
frutas[1] = "Kiwi"
print(frutas[0])

temporada = ["Papaya" , "Melón"]
frutas = frutas + temporada
print(frutas)
frutas.sort()
print(min(frutas) , max(frutas))
print("Cantidad: " , len(frutas))
print(frutas)

nueva_fruta = input("Ingrese una fruta: ")
frutas.append(nueva_fruta)
print(frutas)
frutas .insert(1, 'sandia')
print(frutas)

frutas.remove("Melón")
print(frutas)

if "Uvas" in frutas:
    print("Tenemos uvas en inventario")
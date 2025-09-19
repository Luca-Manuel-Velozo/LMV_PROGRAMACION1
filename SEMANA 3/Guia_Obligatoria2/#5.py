'''5. Buscar un valor:
Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
Informar la posición en caso afirmativo, o indicar que no se encuentra.'''

Num_ent=[0]*10
for i in range(len(Num_ent)):
    Num_ent[i] = int(input(f"ingrese el número en la posición {i+1}:"))

positivo = False
num_usuario = int(input("ingrese el número a buscar: "))
for i in range(len(Num_ent)):
    if Num_ent[i] == num_usuario:
        positivo = True
        posicion = i+1

if positivo == True:
    print(f"El Número solicitado se encuentra en la posición {posicion}")
else:
    print(f"El Número {num_usuario} no está en el array")

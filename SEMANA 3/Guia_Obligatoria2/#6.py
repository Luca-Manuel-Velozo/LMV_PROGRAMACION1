'''6. Mayor y su posición:
Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se
encuentra.'''

Num_ent=[0]*7
for i in range(len(Num_ent)):
    Num_ent[i] = int(input(f"ingrese el número en la posición {i+1}:"))

Num_mayor = Num_ent[0]
for i in range(len(Num_ent)):
    if Num_ent[i]> Num_mayor:
        Num_mayor = Num_ent[i]
        posicion = (i)

print(f"El número mayor es: {Num_mayor} y se encuentra en la posición {posicion}")
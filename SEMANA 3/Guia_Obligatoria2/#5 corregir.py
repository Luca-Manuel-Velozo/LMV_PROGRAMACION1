'''5. Buscar un valor:
Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
Informar la posición en caso afirmativo, o indicar que no se encuentra.'''

Num_ent=[0]*10
Num_ent[0]=1
Num_ent[1]=2
Num_ent[2]=3
Num_ent[3]=4
Num_ent[4]=5
Num_ent[5]=6
Num_ent[6]=7
Num_ent[7]=8
Num_ent[8]=9
Num_ent[9]=10

num_usuario = int(input("ingrese el número a buscar: "))
for num in Num_ent:
    if Num_ent[num] == num_usuario:
        print(f"el número {num_usuario} está dentro del array en la posición {num}")
        break
    else:
        print("no se encuentra el número solicitado")
        break

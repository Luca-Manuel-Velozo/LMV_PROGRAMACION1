'''2. Sumar todos los elementos:
Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los
elementos.'''    

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

sumatotal=0
for i in range(len(Num_ent)):
    sumatotal += Num_ent[i]
print(f"La suma de los elementos del array es: {sumatotal}")
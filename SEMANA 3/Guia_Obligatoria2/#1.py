'''1. Cargar y mostrar array:
Declarar un array de 5 enteros. Cargarlo por teclado y mostrar su contenido por pantalla usando un
ciclo for.'''

Num_ent=[0]*5
Num_ent[0]=1
Num_ent[1]=2
Num_ent[2]=3
Num_ent[3]=4
Num_ent[4]=5
for i in range(len(Num_ent)):
    print(f"El elemento en posición {i+1}: {Num_ent[i]}")
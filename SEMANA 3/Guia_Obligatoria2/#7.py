'''7. Invertir orden:
Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero.'''

Num_ent=[0]*6 
Num_ent[0]=1
Num_ent[1]=2
Num_ent[2]=3
Num_ent[3]=4
Num_ent[4]=5
Num_ent[5]=6

for i in range(len(Num_ent)):
    print(Num_ent[-i-1])

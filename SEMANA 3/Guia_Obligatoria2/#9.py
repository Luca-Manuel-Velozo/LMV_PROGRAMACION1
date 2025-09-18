'''9. Intercambiar elementos pares por ceros:
Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
resultante.'''
import lpm as lpm
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

for i in range(len(Num_ent)):
    if (Num_ent[i]%2) == 0:
        Num_ent[i] = 0
    print(Num_ent[i])



lpm.primera_aparición(Num_ent, 5)

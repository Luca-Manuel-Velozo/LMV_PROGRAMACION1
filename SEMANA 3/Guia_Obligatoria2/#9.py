'''9. Intercambiar elementos pares por ceros:
Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
resultante.'''

Num_ent=[0]*10
for i in range(len(Num_ent)):
    Num_ent[i] = int(input(f"ingrese el número en la posición {i+1}:"))

for i in range(len(Num_ent)):
    if (Num_ent[i]%2) == 0:
        Num_ent[i] = 0
    print(Num_ent[i])



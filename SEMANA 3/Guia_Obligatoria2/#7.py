'''7. Invertir orden:
Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero.'''

Num_ent=[0]*6 
for i in range(len(Num_ent)):
    Num_ent[i] = int(input(f"ingrese el número en la posición {i+1}:"))

for i in range(len(Num_ent)):
    print(Num_ent[-i-1])

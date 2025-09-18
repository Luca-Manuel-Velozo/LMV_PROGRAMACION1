'''8. Comparar dos arrays:
Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
y mostrar un mensaje indicando si son o no iguales.'''

Num_uno=[0]*5
Num_uno[0]=1
Num_uno[1]=2
Num_uno[2]=3
Num_uno[3]=4
Num_uno[4]=5

Num_dos=[0]*5
Num_dos[0]=1
Num_dos[1]=2
Num_dos[2]=3
Num_dos[3]=4
Num_dos[4]=5

igualdad = 0
for i in range(5):
    if Num_uno[i] == Num_dos[i]:
        igualdad += 1
    else:
        
        print("hay disidencia entre los arrays")
        break
if igualdad == 5:
    print("los Arrays son identicos")
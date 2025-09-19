'''8. Comparar dos arrays:
Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
y mostrar un mensaje indicando si son o no iguales.'''

Num_uno=[0]*5
for i in range(len(Num_uno)):
    Num_uno[i] = int(input(f"ingrese el número en la posición {i+1}:"))

Num_dos=[0]*5
for i in range(len(Num_dos)):
    Num_dos[i] = int(input(f"ingrese el número en la posición {i+1}:"))

igualdad = 0
for i in range(5):
    if Num_uno[i] == Num_dos[i]:
        igualdad += 1
    else:
        
        print("hay disidencia entre los arrays")
        break
if igualdad == 5:
    print("los Arrays son identicos")
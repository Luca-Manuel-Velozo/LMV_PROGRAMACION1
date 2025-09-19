'''4. Contar mayores a un valor:
Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado.'''

Num_ent = [0]*8

for i in range(len(Num_ent)):
    Num_ent[i] = int(input(f"ingrese el número en la posición {i+1}:"))

contador = 0

for num in Num_ent:
    if num > 100:
        contador += 1

print(f"Cantidad de elementos mayores a 100: {contador}")
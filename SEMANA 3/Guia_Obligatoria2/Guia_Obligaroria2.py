'''1. Cargar y mostrar array:
Declarar un array de 5 enteros. Cargarlo por teclado y mostrar su contenido por pantalla usando un
ciclo for.
2. Sumar todos los elementos:
Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los
elementos.
3. Promedio de valores:
Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio
de los valores.
4. Contar mayores a un valor:
Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado.
5. Buscar un valor:
Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
Informar la posición en caso afirmativo, o indicar que no se encuentra.
6. Mayor y su posición:
Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se
encuentra.
7. Invertir orden:
Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero.
8. Comparar dos arrays:
Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
y mostrar un mensaje indicando si son o no iguales.
9. Intercambiar elementos pares por ceros:
Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
resultante.
10. Función para buscar la primera aparición de un valor:
Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar
la posición de la primera aparición de ese número o -1 si no se encuentra.
'''

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

'''3. Promedio de valores:
Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio
de los valores.'''

Num_flo=[0.0]*6
Num_flo[0]=1
Num_flo[1]=2
Num_flo[2]=3
Num_flo[3]=4
Num_flo[4]=5
Num_flo[5]=6

sumatotal=0
for i in range(len(Num_flo)):
    sumatotal += Num_flo[i]

promedio=sumatotal/len(Num_flo)
print(f"el promedio de los elementos del array es: {promedio}")

'''4. Contar mayores a un valor:
Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado.'''

Num_ent = [0]*8
Num_ent[0] = 50
Num_ent[1] = 120
Num_ent[2] = 101
Num_ent[3] = 99
Num_ent[4] = 200
Num_ent[5] = 80
Num_ent[6] = 150
Num_ent[7] = 60

contador = 0
for num in Num_ent:
    if num > 100:
        contador += 1

print(f"Cantidad de elementos mayores a 100: {contador}")

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
    if num_usuario == Num_ent[num]:
        print(f"el número {num_usuario} está dentro del array en la posición {num}")
        break
    else:
        print("no se encuentra el número solicitado")
        break

        
'''6. Mayor y su posición:
Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se
encuentra.'''

Num_ent=[0]*10
Num_ent[0]=1
Num_ent[1]=2
Num_ent[2]=3
Num_ent[3]=5
Num_ent[4]=4
Num_ent[5]=7
Num_ent[6]=6

Num_mayor = Num_ent[0]
for i in range(len(Num_ent)):
    if Num_ent[i]> Num_mayor:
        Num_mayor = Num_ent[i]
        posicion = (i)

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

print(f"El número mayor es: {Num_mayor} y se encuentra en la posición {posicion}")

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
Num_dos[0]=4
Num_dos[1]=2
Num_dos[2]=3
Num_dos[3]=4
Num_dos[4]=5

for i in range(5):
    if Num_uno[i] == Num_dos[i]:
        print("los Arrays son identicos")
    else:
        print("hay disidencias")
        break

'''9. Intercambiar elementos pares por ceros:
Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
resultante.'''

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

'''10. Función para buscar la primera aparición de un valor:
Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar
la posición de la primera aparición de ese número o -1 si no se encuentra.'''


def primera_aparición(array, numero):
    posicion = 0 
    for i in range(len(array)):
        if array[i] == numero:
            posicion = i
            break
        else:
            posicion = -1
    return posicion

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
    return print(posicion)


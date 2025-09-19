'''5. Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si
es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función.'''

def es_par(num):
    if (num%2) == 0:
        paridad= True
    else :
        paridad= False
    return (paridad)
    
num = int(input("ingrese un número para determinar su paridad: "))
paridad=es_par(num)
if paridad is True:
    print("es par")
else :
    print("no es par")

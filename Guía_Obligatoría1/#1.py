'''#1 1. Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima
un saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función.'''

def saludar(nombre):
    saludo = ("hola, "+nombre+", cómo estás?")
    return print(saludo)

nombre=input("Introduzca su nombre: " )
saludar(nombre)

'''2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma,
resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la
función.'''
def operaciones(num1, num2):
    suma = num1+num2
    resta = num1-num2
    multi = num1*num2
    print("el resultado de la suma es ", suma)
    print("el resultado de la resta es ", resta)
    print("el resultado de la multiplicación es ", multi)

num1 = int(input("ingrese el primer número: "))
num2 = int(input("ingrese  el segundo número: "))
operaciones(num1, num2)

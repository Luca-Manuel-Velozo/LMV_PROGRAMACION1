'''3. Definir una función area_triangulo que reciba la base y la altura de un triángulo y
devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado.
Fórmula: area = (b * h) / 2.'''


def area_triangulo(base,altura):
    area = float(base * altura)/2
    print(f"el área del triángulo es: {area}cm")

print ("Calculadora de Área de un triángulo")
base = float(input("Ingrese la longitud de la base del triángulo(cm): "))
altura = float(input("Ingrese la altura del triángulo(cm):"))
area_triangulo(base,altura)



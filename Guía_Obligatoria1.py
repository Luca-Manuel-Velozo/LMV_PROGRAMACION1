'''1. Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima
un saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función.
2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma,
resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la
función.
3. Definir una función area_triangulo que reciba la base y la altura de un triángulo y
devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado.
Fórmula: area = (b * h) / 2.
4. Crear una función buscar_mayor que reciba tres números y devuelva los tres números
ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números
ordenados.
5. Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si
es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función.
6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva
cuántas horas y minutos sobran.
7. Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si
es mayor de edad (18 años o más) devolviendo un booleano. Luego, el programa debe pedir la
edad al usuario y mostrar un mensaje apropiado.
8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y
devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el
año de nacimiento del usuario y mostrar la edad calculada.

'''
#1
def saludar(nombre)
    saludo = "hola, ",nombre ", cómo estás?"
    return print(saludo)

nombre=input("Introduzca su nombre: " )
Saludar(nombre)

#2
def operaciones(num1, num2)
    Suma = num1+num2
    Resta = num1-num2
    Multi = num1*num2
    return print("el resultado de la suma es ", Suma)
    print("el resultado de la resta es ", Resta)
    print("el resultado de la multiplicación es ", Multi)

num1 = input( "ingresé el primer número: ")
num2 = input( "ingresé  el segundo número: ")
saludar(num1, num2)

#3
def area_triangulo(base,altura)
    area = (base * altura)/2
    return area

print ("Calculadora de Área de un triángulo")
base = input("Ingrese la longitud de la base del triángulo(cm): ")
altura = input("Ingrese la altura del triángulo(cm):")
print("el área del triángulo es:")
area_triangulo(base,altura)

#4
def buscar_mayor(a,b,c)
    if b<a>c
        1ero=a
        if b>c
            2do=b
            3ro=c
        else
            2do=c
            3ro=b
    elif a<b>c
        1ero=b
        if a>c
            2do=a
            3ro=c
        else
            2do=c
            3ro=a
    else 
        1ero=c
        if a>b
            2do=a
            3ro=b
        else
            2do=b
            3ro=a
    return (1ero,2do,3ro)

print("ingrese tres números para ser ordenados de mayor a menor")
num1=input(int("primer número: "))
num2=input(int("segundo número: "))
num3=input(int("tercer número: "))

print("ordenados quedan:")
buscar_mayor(num1,num2,num3):

#5
def es_par(num)
    if num%2 = 0
        paridad= true
    else 
        paridad= false
    return (paridad)
    
num = input("ingrese un número para determinar su paridad: ")
es_par(num)
if paridad is true
    print("es par")
else 
    print("no es par")
    
#6

def convertir_minutos(mins):
    horas= int(mins//60)
    sobrante= int(mins%60)
    return (horas,sobrante)
    

#7

def
    
    

        
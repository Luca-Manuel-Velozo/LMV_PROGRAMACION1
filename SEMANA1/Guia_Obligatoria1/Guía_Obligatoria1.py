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
año de nacimiento del usuario y mostrar la edad calculada.'''



'''#1 1. Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima
un saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función.'''

def saludar(nombre):
    saludo = ("hola, "+nombre+", cómo estás?")
    return print(saludo)

nombre=input("Introduzca su nombre: " )
saludar(nombre)

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

'''4. Crear una función buscar_mayor que reciba tres números y devuelva los tres números
ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números
ordenados.'''

def buscar_mayor(a,b,c):
    if b<a>c:
        pro=a
        if b>c:
            sdo=b
            tro=c
        else:
            sdo=c
            tro=b
    elif a<b>c:
        pro=b
        if a>c:
            sdo=a
            tro=c
        else:
            sdo=c
            tro=a
    else:
        pro=c
        if a>b:
            sdo=a
            tro=b
        else:
            sdo=b
            tro=a
    return print(pro,sdo,tro)

print("ingrese tres números para ser ordenados de mayor a menor")
num1=int(input("primer número: "))
num2=int(input("segundo número: "))
num3=int(input("tercer número: "))

print("ordenados quedan:")
buscar_mayor(num1,num2,num3)

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

    
'''6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva
cuántas horas y minutos sobran.'''

def convertir_minutos(mins):
    horas= int(mins//60)
    sobrante= int(mins%60)
    return (horas,sobrante)
    
'''7. Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si
es mayor de edad (18 años o más) devolviendo un booleano. Luego, el programa debe pedir la
edad al usuario y mostrar un mensaje apropiado.'''

def verificar_acceso(edad):
    if edad >= 18:
        pasa=True
        
    else :
        pasa=False
    return pasa
    
edad=int(input("ingrese su edad: "))
acceso=verificar_acceso(edad)
if acceso==True:
    print("Acceso concedido")
else:
    print("Acceso denegado")
    
'''8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y
devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el
año de nacimiento del usuario y mostrar la edad calculada.'''    

def calcular_edad(anio_nacimiento):
    edad=int(2025-anio_nacimiento)
    return edad
anio_nacimiento=int(input("ingrese el año de nacimiento para calcular la edad: "))
edad=calcular_edad(anio_nacimiento)
print(f"la edad calculada es de {edad} años")
    
    

        
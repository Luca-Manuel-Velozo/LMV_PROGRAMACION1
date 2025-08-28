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
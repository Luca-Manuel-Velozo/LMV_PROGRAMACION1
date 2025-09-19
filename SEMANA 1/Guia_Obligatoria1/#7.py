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
    
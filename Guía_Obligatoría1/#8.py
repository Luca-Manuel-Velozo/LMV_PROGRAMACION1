'''8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y
devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el
año de nacimiento del usuario y mostrar la edad calculada.'''    

def calcular_edad(anio_nacimiento):
    edad=int(2025-anio_nacimiento)
    return edad
anio_nacimiento=int(input("ingrese el año de nacimiento para calcular la edad: "))
edad=calcular_edad(anio_nacimiento)
print(f"la edad calculada es de {edad} años")
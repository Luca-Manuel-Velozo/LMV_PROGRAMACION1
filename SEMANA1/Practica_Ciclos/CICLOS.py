'''1. Ingreso de datos secuenciales
○ Pedir el nombre y edad de un visitante.
○ Pedir cuántas atracciones quiere usar (por ahora, el parque tiene solo 3 atracciones: Montaña
Rusa, Casa del Terror y Carrusel).
2. Uso de condicionales
○ Determinar si el visitante puede subir a la Montaña Rusa (solo si tiene 12 años o más).
○ Si el visitante tiene menos de 6 años, solo puede subir al Carrusel.
○ Los demás pueden acceder a todas las atracciones.
3. Uso de ciclos
○ Preguntar por cada atracción que el visitante desea usar y mostrar si puede subir o no según
su edad.
○ Calcular el costo total de las entradas (ejemplo: Montaña Rusa = $1500, Casa del Terror =
$1200, Carrusel = $800).
4. Salida de resultados
○ Mostrar un resumen con el nombre del visitante, la lista de atracciones que eligió, cuáles pudo
usar y el costo total a pagar.'''

print("¡¡Bienvenido a PythonLand!!")
nombre=str(input("Ingrese su nombre: "))
edad=int(input("Ingrese su Edad: "))
atracciones=int(input("cuántas atracciones desea usar?(Máximo 3): "))

if edad>=12:
    carrusel = True
    casa_terror = True
    mrusa = True
elif edad>=6:
    carrusel = True
    casa_terror = True
    mrusa = False
else:
    carrusel = True
    casa_terror = False
    mrusa = False
atracc=["Carrusel","Casa del Terror","Montaña Rusa"]
total=0
for eleccion in atracc:
    print(f"{eleccion}")
    if eleccion == "Carrusel":
        print("subis al Carrusel?")
        subeC=str(input("SI/NO(usar mayúsculas):"))
        if subeC=="SI":
            subeC=True
            if carrusel==False:
                print("No puede acceder a ésta atracción")
            else:
    if eleccion == "Casa del Terror":
        print("subis a la Casa del Terror?")
        subeCT=str(input("SI/NO(usar mayúsculas):"))
        if subeCT=="SI":
            subeCT=True
            if casa_terror==False:
                print("No puede acceder a ésta atracción")
            else:
                total =+2000       
    if eleccion == "Montaña Rusa":
        print("subis a la Montaña Rusa?")
        subeMR=str(input("SI/NO(usar mayúsculas):"))
        if subeMR=="SI":
            subeMR=True
            if mrusa==False:
                print("No puede acceder a ésta atracción")
            else:
                total =+3000   
usadas={subeMR,subeC,subeCT}

print(total)    


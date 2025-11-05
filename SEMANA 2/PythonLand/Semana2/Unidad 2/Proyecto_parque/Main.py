import Gestion_Parque.Parque as GP


print("¡¡Bienvenido a PythonLand!!")
nombre=str(input("\nIngrese su nombre: "))
edad=int(input("Ingrese su Edad: "))
atracciones=int(input("cuántas atracciones desea usar?(Máximo 3): "))

carrusel = GP.puede_subir(edad,"carrusel")
mrusa = GP.puede_subir(edad,"mrusa")
casa_terror = GP.puede_subir(edad,"casa_terror")


total=0
subtotal=0
elegidas=0
for eleccion in range(atracciones):
    print(f"{eleccion}")
    match eleccion:

        case "\nCarrusel":
            print("-subis al Carrusel?")
            subeC=str(input("SI/NO(usar mayúsculas):"))
            if subeC=="SI":
                if elegidas<atracciones:
                    subeC=True
                    if carrusel==False:
                        print("\nNo puede acceder a ésta atracción")
                    else:
                        subtotal = subtotal+1500
                        elegidas=elegidas+1
                else:
                    print("no podes elegir más atracciones")
        case "\nCasa del Terror":
            print("-subis a la Casa del Terror?")
            subeCT=str(input("SI/NO(usar mayúsculas):"))
            if subeCT=="SI":
                if elegidas<atracciones:
                    subeCT=True
                    if casa_terror==False:
                        print("\nNo puede acceder a ésta atracción")
                    else:
                        subtotal = subtotal+2000
                        elegidas=elegidas+1
                else:
                    print("no podes elegir más atracciones")
        case "\nMontaña Rusa":
            print("subis a la Montaña Rusa?")
            subeMR=str(input("SI/NO(usar mayúsculas):"))
            if subeMR=="SI":
                if elegidas<atracciones:
                    subeMR=True
                    if mrusa==False:
                        print("\nNo puede acceder a ésta atracción")
                    else:
                        subtotal = subtotal+3000
                        elegidas=elegidas+1   
                else:
                    print("no podes elegir más atracciones")
subio=[carrusel,casa_terror,mrusa]

print("\nRegistro de Visitante")
print(f"\nNombre:{nombre}")
if subeC == True:
    print("Carrusel elegido")
    if carrusel==True:
        print("     Pudo subir")
if subeCT == True:
    print("Casa del Terror elegida")
    if casa_terror==True:
        print("     Pudo subir")  
if subeMR == True:
    print("Montaña Rusa elegida")
    if mrusa==True:
        print("     Pudo subir")
print(f"Subtotal: ${subtotal}")
if atracciones>=3 and carrusel==True and mrusa==True and casa_terror==True:
    total = subtotal-(subtotal*10/100)
else:
    total = subtotal
print(f"    Total: ${total}")

def puede_subir(edad,atraccion):
    edad = int(input("Ingrese la edad del visitante: "))
    if edad >= 12:
        Subemr = True
        Subect = True
        Subecs = True
    elif 12 > edad >= 6:
        Subemr = False
        Subect = True
        Subecs = True
    else:
        Subemr = False
        Subect = False
        Subecs = True


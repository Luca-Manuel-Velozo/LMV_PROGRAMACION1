def mostrar_atracciones():
    print("ATRACCIONES DE PYTHONLAND")
    print("\n1- Carrusel")
    print("\n2- Casa del Terror")
    print("\n3- Montaña Rusa")

def puede_subir(edad,atraccion):
    if edad >= 12:
        puedemr = True
        puedect = True
        puedecs = True
    elif 12 > edad >= 6:
        puedemr = False
        puedect = True
        puedecs = True
    else:
        puedemr = False
        puedect = False
        puedecs = True
    if atraccion == 1:
        print(f"¿Puede subir al Carrusel?: {puedecs}")
    elif atraccion == 2:
        print(f"¿Puede entrar a la Casa del terror?: {puedect}")
    elif atraccion == 3:
        print(f"¿Puede subir a la Montaña Rusa?: {puedemr}")
    else:
        print("Atracción no encontrada... intente denuevo.")

def evaluacion_edad(edad):
    if edad >= 12:
        puedemr = True
        puedect = True
        puedecs = True
    elif 12 > edad >= 6:
        puedemr = False
        puedect = True
        puedecs = True
    else:
        puedemr = False
        puedect = False
        puedecs = True
    return puedecs, puedect, puedemr
    
def calcular_precio(atraccion):
    if atraccion == 1:
        print("Carrusel: -$1.500")
    elif atraccion == 2:
        print("Casa del Terror: -$2.000")
    elif atraccion == 3:
        print("Montaña Rusa: -$3.000")
    else:
        print("Atracción no encontrada... intente denuevo.")

def registrar_visita():
    nombre=str(input("\nIngrese su nombre: "))
    atracciones = 0
    while atracciones == 0:
        edad=int(input("Ingrese su Edad: "))
        if edad >= 12:
            atracciones=int(input("cuántas atracciones desea usar?(Máximo 3): "))
        elif 12 > edad >= 6:
            atracciones=int(input("cuántas atracciones desea usar?(Máximo 2): "))
        elif edad < 6:
            atracciones = 1
            print("De momento solo podes subir al Carrusel...")
        else:
            print("valor no válido, intentá denuevo...")   
    elecciones = 0
    total = 0
    subtotal = 0
    while elecciones != atracciones:
        puedecs, puedect, puedemr = evaluacion_edad(edad)
        print("-ELECCIÓN DE ATRACCIONES ACCESIBLES-")
        subecs = ""
        subect = ""
        subemr = ""
        if  puedecs == True:
            while subecs != "s" and subecs != "n":
                subecs = input("Carrusel(s/n): ")
            if subecs == "s":
                subtotal += 1500
                elecciones += 1
                subecs = True
            else:
                subecs = False
        else:
            print("No puede subir al Carrusel") 
        
        if  puedect == True:
            while subect != "s" and subect != "n":
                subect = input("Casa del Terror(s/n): ")
            if subect == "s":
                subtotal += 2000
                elecciones += 1
                subect = True
            else:
                subect = False
        else:
            print("No puede subir a la Casa del Terror")
        
        if  puedemr == True:
            while subemr != "s" and subemr != "n":
                subemr = input("Montaña Rusa(s/n): ")
            if subemr == "s":
                subtotal += 3000
                elecciones += 1
                subemr = True
            else:
                subemr = False
        else:
            print("No puede subir a la Montaña Rusa")
        exit = input("Desea salir del Menú?(s/n): ")
        if exit == "s":
            break
        else:
            pass
    if elecciones == atracciones:
        print("MÁXIMO DE ATRACCIONES ALCANZADO")
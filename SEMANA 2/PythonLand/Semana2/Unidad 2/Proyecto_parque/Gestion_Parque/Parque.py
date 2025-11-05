def mostrar_atracciones():
    print("ATRACCIONES DE PYTHONLAND")
    print("\n1- Carrusel")
    print("\n2- Casa del Terror")
    print("\n3- Montaña Rusa")

def puede_subir(edad,atraccion):
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
    if atraccion == 1:
        print(f"¿Puede subir al Carrusel?: {Subecs}")
    elif atraccion == 2:
        print(f"¿Puede entrar a la Casa del terror?: {Subect}")
    elif atraccion == 3:
        print(f"¿Puede subir a la Montaña Rusa?: {Subemr}")
    else:
        print("Atracción no encontrada... intente denuevo.")
    
def calcular_precio(atraccion):
    match atraccion:
        case "carrusel":
            print("-$1.500")
        case "mrusa":
            print("-$3.000")
        case "casa_terror":
            print("-$2.000")
        case _:
            print("Opción inválida")

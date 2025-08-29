def mostrar_atracciones():
    print("ATRACCIONES DE PYTHONLAND")
    print("\nCarrusel")
    print("\nCasa del Terror")
    print("\nMontaña Rusa")
def puede_subir(edad,atraccion):
    match atraccion:
        case "carrusel":
            if edad>=12:
                carrusel = True
            elif edad>=6:
                carrusel = True
            else:
                carrusel = True
            return carrusel
        case "casa_terror":
            if edad>=12:
                casa_terror = True
            elif edad>=6:
                casa_terror = True
            else:
                casa_terror = False
            return casa_terror
        case "mrusa":
            if edad>=12:
                mrusa = True
            elif edad>=6:
                mrusa = False
            else:
                mrusa = False
            return mrusa        
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

def cargar_titulos(titulos, ejemplares):
    for i in range(len(titulos)):
        titulos[i] = input("ingrese el nombre del título: ")
        if titulos[i] == "":
            break
        ejemplares[i] = input("ingrese la cantidad de ejemplares: ")

def mostrar_catalogo(titulos, ejemplares):
    for i in range(MAX_LIBROS):
        print(f"\nTitulo: {titulos[i]}")
        print(f"Cantidad de ejemplares: {ejemplares[i]}")
        
def consultar_disponibilidad(titulos, ejemplares):
    disponibilidad = input("ingrese el título que busca: ")
    for i in range(MAX_LIBROS):
        if titulos[i] == disponibilidad:
            cantidad = ejemplares[i]
            print(f"Éste titulo tiene {cantidad} ejemplares")

def listar_agotados(titulos, ejemplares):
    print("Títulos agotados:\n")
    for i in range(MAX_LIBROS):
        if ejemplares[i] == 0:
            print(titulos[i])

def agregar_titulo(titulos, ejemplares):
    for i in range(MAX_LIBROS):
        if titulos[i] == "":
            titulos[i] = input("ingrese el nombre del título: ")
            if titulos[i] == "":
                break
            ejemplares[i] = input("ingrese la cantidad de ejemplares: ")

def actualizar_ejemplares(titulos, ejemplares):
    for i in range(MAX_LIBROS):
        print(f"{i+1}- Titulo: {titulos[i]}")
    valido = False
    while valido == False:
        cambio = input("\nSeleccione el numero de lista del título a modificar: ")

        if cambio != [i+1]:
            valido = False
        else:
            ejemplares[i] = input("ingrese la cantidad actualizada: ")
            valido = True
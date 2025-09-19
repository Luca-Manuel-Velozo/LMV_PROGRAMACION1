def cargar_titulos(titulos, ejemplares, MAX_LIBROS):
    for i in range(len(titulos)):
        titulos[i] = input("\ningrese el nombre del título: ")
        if titulos[i] == "":
            break
        ejemplares[i] = int(input("ingrese la cantidad de ejemplares: "))

def mostrar_catalogo(titulos, ejemplares, MAX_LIBROS):
    for i in range(MAX_LIBROS):
        if titulos[i] == "":
            break
        print(f"\nTitulo: {titulos[i]}")
        print(f"Cantidad de ejemplares: {ejemplares[i]}")
        
        
def consultar_disponibilidad(titulos, ejemplares,MAX_LIBROS):
    disponibilidad = input("\ningrese el título que busca: ")
    for i in range(MAX_LIBROS):
        if titulos[i] == disponibilidad:
            cantidad = ejemplares[i]
            print(f"\nÉste titulo tiene {cantidad} ejemplares")
        else:
            print("No se encuentra disponible")

def listar_agotados(titulos, ejemplares, MAX_LIBROS):
    print("Títulos agotados:\n")
    for i in range(len(titulos)):
        if ejemplares[i] == 0:
            print(titulos[i])

def agregar_titulo(titulos, ejemplares, MAX_LIBROS):
    for i in range(MAX_LIBROS):
        if titulos[i] == "":
            titulos[i] = input("\ningrese el nombre del título: ")
            if titulos[i] == "":
                break
            ejemplares[i] = int(input("ingrese la cantidad de ejemplares: "))

def actualizar_ejemplares(titulos, ejemplares, MAX_LIBROS):
    indicador = [0]*20
    for i in range(MAX_LIBROS):
        if titulos[i] == "":
            break
        print(f"{i+1}- Titulo: {titulos[i]}")
        indicador[i] = (i+1)
        
    valido = False

    while valido == False:
        cambio = int(input("\nSeleccione el numero de lista del título a modificar: "))
        ejemplares[cambio-1] = input("ingrese la cantidad actualizada: ")
        valido = True
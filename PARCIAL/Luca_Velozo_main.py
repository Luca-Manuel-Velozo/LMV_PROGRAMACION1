MAX_ALUMNOS = 10
lista_alumnos = [""] * MAX_ALUMNOS
lista_libros = [0] * MAX_ALUMNOS
lista_comentarios = [""] * MAX_ALUMNOS

def cargar_alumnos(MAX_ALUMNOS, lista_alumnos, lista_libros, lista_comentarios):
    for i in range(MAX_ALUMNOS):

        while True:
            lista_alumnos[i] = input("\nNombre Completo: ")
            if lista_alumnos[i] == "":
                print("No puede dejar el campo vacio!")
                continue
            break

        while True:
            lista_libros[i] = int(input("Libros leídos: "))
            if lista_libros[i] >= 21 or lista_libros[i] <= 0 :
                print("Ingrese una cantidad entre 1 y 20")
                continue
            break

        while True:
            lista_comentarios[i] = input("Comentario: ")
            if lista_comentarios[i] == "":
                print("No puede dejar el campo vacio!")
                continue
            break

        sigo = input("\nDesea ingresar otro alumno?(s/n): ").lower()
        if sigo == "n":
            break
        elif sigo == "s":
            pass
        else:
            break

def mostrar_habitos(MAX_ALUMNOS, lista_alumnos, lista_libros, lista_comentarios):
    libros=0
    alumnos=0
    for i in range(MAX_ALUMNOS):
        if lista_alumnos[i] == "":
            print(f"\nEl promedio de libros leídos fué de {libros//alumnos} libros por alumno")
            break
        print(f"\nAlumno {i+1}: \n")
        print(f"Nombre Completo: {lista_alumnos[i]}")
        print(f"Libros leídos: {lista_libros[i]}")
        print(f"Comentario: {lista_comentarios[i]}")
        libros += lista_libros[i]
        alumnos = i+1

def ordenar(lista_alumnos, lista_libros, lista_comentarios):
    n = len(lista_libros)

    for i in range(n-1):

        intercambio = False

        for j in range(n-1-i):
            if lista_libros[j] != 0 and lista_libros[j+1] != 0: 
                if lista_libros[j] < lista_libros[j+1]:
                    lista_libros[j], lista_libros[j+1] = lista_libros[j+1], lista_libros[j]
                    lista_alumnos[j], lista_alumnos[j+1] = lista_alumnos[j+1], lista_alumnos[j]
                    lista_comentarios[j], lista_comentarios[j+1] = lista_comentarios[j+1], lista_comentarios[j]
                    intercambio = True

        if intercambio == False:
            break
    print ("\nLista Ordenada en forma descendente: ")

while True:
    print("\n===        Menú        ===")
    print("=== Hábitos de lectura ===\n")
    print("1. Cargar Alumnos")
    print("2. Mostrar hábitos de lectura")
    print("3. Ordenar Alumnos por cantidad de libros leídos")
    print("4. Salir")
    opcion = input("\nSeleccione una opción: ")
    if opcion == "1":
        cargar_alumnos(MAX_ALUMNOS, lista_alumnos, lista_libros, lista_comentarios)
    elif opcion == "2":
        mostrar_habitos(MAX_ALUMNOS, lista_alumnos, lista_libros, lista_comentarios)
    elif opcion == "3":
        ordenar(lista_alumnos, lista_libros, lista_comentarios)
        mostrar_habitos(MAX_ALUMNOS, lista_alumnos, lista_libros, lista_comentarios)
    elif opcion == "4":
        print("recolección de información Finalizada!!... \n...Cerrando.")
        break
    else:
        print("\nOpcion Invalida. Vuelva a intentar...\n")
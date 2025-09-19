'''Una biblioteca escolar necesita un pequeño sistema de gestión para su catálogo de libros.
Se deben usar listas estáticas con un máximo de 20 títulos y sus respectivos ejemplares.
Requerimientos:
1. Usar dos listas paralelas:
1. titulos[] → nombres de los libros.
2. ejemplares[] → cantidad de copias disponibles.
Cada índice representa el mismo libro en ambas listas.
2. Implementar un menú de opciones utilizando un bucle while que se repita hasta que el usuario elija
Salir.
3. Opciones del menú:
1. Cargar títulos y ejemplares
Permitir al usuario ingresar hasta 20 títulos y la cantidad de ejemplares para cada uno.
2. Mostrar catálogo completo
Listar cada título con su número de ejemplares.
Ejemplo: El Señor de los Anillos → 5 copias
3. Consultar disponibilidad
Pedir al usuario un título y mostrar cuántas copias tiene.
4. Listar títulos agotados
Mostrar solo aquellos títulos que tengan 0 copias.
5. Agregar un nuevo título
Permitir al usuario agregar un nuevo libro y su cantidad de ejemplares si no se superó el máximo
de 20.
6. Actualizar ejemplares (préstamo / devolución)
Permitir al usuario modificar el número de ejemplares de un libro existente.
7. Salir
Ejemplo de listas paralelas:
titulos = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
ejemplares = [5, 3, 7]
Puntos clave:
● Usar listas estáticas de tamaño fijo ([""] * 20 y [0] * 20).
● Manejar correctamente los índices para mantener sincronizados títulos y ejemplares.
● Evitar sobrepasar el límite de 20 elementos.
● Modularizar usando funciones para cada opción del menú.'''

import funciones as Fc

MAX_LIBROS = 20
titulos = [""] * MAX_LIBROS
ejemplares = [0] * MAX_LIBROS

while True:
    print("\n=== Menú Biblioteca ===\n")
    print("1. Cargar títulos y ejemplares")
    print("2. Mostrar catálogo completo")
    print("3. Consultar disponibilidad")
    print("4. Listar títulos agotados")
    print("5. Agregar un nuevo título")
    print("6. Actualizar ejemplares (préstamo / devolución)")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        Fc.cargar_titulos(titulos, ejemplares, MAX_LIBROS)
    elif opcion == "2":
        Fc.mostrar_catalogo(titulos, ejemplares, MAX_LIBROS)
    elif opcion == "3":
        Fc.consultar_disponibilidad(titulos, ejemplares, MAX_LIBROS)
    elif opcion == "4":
        Fc.listar_agotados(titulos, ejemplares, MAX_LIBROS)
    elif opcion == "5":
        Fc.agregar_titulo(titulos, ejemplares, MAX_LIBROS)
    elif opcion == "6":
        Fc.actualizar_ejemplares(titulos, ejemplares, MAX_LIBROS)
    elif opcion == "7":
        print("Nos vemos!")
        break
    else:
        print("Opción no válida. Intente de nuevo.\n")


            



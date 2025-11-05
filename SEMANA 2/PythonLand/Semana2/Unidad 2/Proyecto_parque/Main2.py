import Gestion_Parque.Parque as pp


print("\n¡¡Bienvenido a PythonLand!!\n")
while True:
    print("=== Menú Del Parque ===")
    print("1- Mostrar atracciones")
    print("2- ¿Puedo subir a las atracciones?")
    print("3- Calcular precio de la atracción")
    print("4- Registrá tu visita!")
    print("5- Resumen de visita")
    print("6- SALIR")
    opcion = input("---Seleccione una opción: ")
    if opcion == "1":
        pp.mostrar_atracciones()
    elif opcion == "2":
        edad = int(input("Ingrese la edad del visitante: "))
        pp.mostrar_atracciones()    
        atraccion = int(input("\nIngrese el número de la atracción a verificar: "))
        pp.puede_subir(edad,atraccion)
    elif opcion == "3":
        pp.mostrar_atracciones()
        atraccion = int(input("\nIngrese el número de la atracción a calcular: "))
        pp.puede_subir(edad,atraccion)
        pp.calcular_precio()
    elif opcion == "4": 
        pp.registrar_visita()
    elif opcion == "5":
        pp.mostrar_resumen()
    elif opcion == "6":
        print("Nos vemos!")
        break
    else:
        print("Opción no válida. Intente de nuevo.\n")
    
        
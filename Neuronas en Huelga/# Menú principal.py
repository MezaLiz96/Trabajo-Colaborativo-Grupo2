# Menú principal
def menu2():
    while True:
        print("1. Registrar alumno")
        print("2. Mostrar alumnos")
        print("3. Calcular promedio")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_alumno()
        elif opcion == "2":
            mostrar_alumnos()
        elif opcion == "3":
            calcular_promedio()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida\n")
from archivo_funciones import agregar_compra, mostrar_compras, mostrar_total
compras = []
total_gastado = 0

while True:
    print(" ")
    print("Menú:")
    print("1. Agregar compra")
    print("2. Mostrar compras")
    print("3. Mostrar total gastado")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        producto = input("Ingresa el nombre del producto: ")
        monto = float(input("Ingresa el monto gastado: "))
        agregar_compra(compras, producto, monto)
        total_gastado += monto

    elif opcion == "2":
        mostrar_compras(compras)

    elif opcion == "3":
        mostrar_total(compras)

    elif opcion == "4":
        print("Gracias por utilizar el programa.")
        break  # Salir del bucle while

    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
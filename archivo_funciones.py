def agregar_compra(lista_de_compras, producto, monto):
    compra = (producto, monto)
    lista_de_compras.append(compra)
    print(f"La compra de '{producto}' por {monto} se ha agregado correctamente a la lista de compras.")


def mostrar_compras(lista_de_compras):
    if not lista_de_compras:
        print("No hay compras registradas.")
    else:
        print("Lista de compras:")
        for i, compra in enumerate(lista_de_compras, 1):
            producto, monto = compra
            print(f"Compra {i}: {producto} - Monto: {monto}")


def mostrar_total(lista_de_compras):
    if not lista_de_compras:
        print("No hay compras registradas.")
    else:
        total = sum(monto for _, monto in lista_de_compras)
        total_formateado = "${:.2f}".format(total)  # Formatear como valor monetario
        print(f"Total gastado: {total_formateado}")

from inventario import Inventario

if __name__ == "__main__":
    inventario = Inventario()

    # Añadir productos
    inventario.añadir_producto(1, "Camiseta", 50, 15.99)
    inventario.añadir_producto(2, "Pantalón", 30, 25.50)

    # Mostrar inventario
    inventario.mostrar_inventario()

    # Buscar producto
    inventario.buscar_producto("Camiseta")

    # Actualizar producto
    inventario.actualizar_producto(1, cantidad=40)

    # Eliminar producto
    inventario.eliminar_producto(2)

    # Mostrar inventario después de la actualización y eliminación
    inventario.mostrar_inventario()

    from inventario import Inventario


    def mostrar_menu():
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")


    if __name__ == "__main__":
        inventario = Inventario()

        # Añadir productos iniciales
        inventario.añadir_producto(1, "Camiseta", 50, 15.99)
        inventario.añadir_producto(2, "Pantalón", 30, 25.50)

        # Mostrar inventario inicial
        inventario.mostrar_inventario()

        while True:
            # Mostrar el menú interactivo
            mostrar_menu()
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                # Añadir producto
                id_producto = int(input("Ingresa el ID del producto: "))
                nombre = input("Ingresa el nombre del producto: ")
                cantidad = int(input("Ingresa la cantidad del producto: "))
                precio = float(input("Ingresa el precio del producto: "))
                inventario.añadir_producto(id_producto, nombre, cantidad, precio)

            elif opcion == "2":
                # Mostrar inventario
                inventario.mostrar_inventario()

            elif opcion == "3":
                # Buscar producto
                nombre_buscar = input("Ingresa el nombre del producto a buscar: ")
                inventario.buscar_producto(nombre_buscar)

            elif opcion == "4":
                # Actualizar producto
                id_producto = int(input("Ingresa el ID del producto a actualizar: "))
                cantidad = input("Ingresa la nueva cantidad (deja en blanco si no deseas actualizarla): ")
                precio = input("Ingresa el nuevo precio (deja en blanco si no deseas actualizarlo): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)

            elif opcion == "5":
                # Eliminar producto
                id_producto = int(input("Ingresa el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)

            elif opcion == "6":
                # Salir
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida, por favor selecciona nuevamente.")
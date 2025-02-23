# Clase Producto: Representa un producto en el inventario
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

# Clase Inventario: Maneja la lista de productos y la interacción con el archivo
class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    # Carga el inventario desde el archivo
    def cargar_inventario(self):
        try:
            # Si el archivo no existe, lo crea automáticamente
            with open(self.archivo, 'a+') as f:
                f.seek(0)  # Mueve el puntero al inicio del archivo
                for linea in f:
                    try:
                        id, nombre, cantidad, precio = linea.strip().split(',')
                        self.productos.append(Producto(int(id), nombre, int(cantidad), float(precio)))
                    except ValueError:
                        print(f"Advertencia: Línea de archivo malformada: {linea}")
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("El archivo de inventario no existe. Se creará uno nuevo.")
            with open(self.archivo, 'w'): pass  # Crear el archivo vacío si no existe
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    # Guarda el inventario en el archivo
    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos:
                    f.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except IOError:
            print("Error de entrada/salida al intentar guardar el inventario.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    # Añade un nuevo producto al inventario
    def añadir_producto(self, producto):
        self.productos.append(producto)
        self.guardar_inventario()
        print(f"Producto {producto.nombre} añadido exitosamente.")

    # Actualiza un producto existente en el inventario
    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id == id:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_inventario()
                print(f"Producto {producto.nombre} actualizado exitosamente.")
                return
        print(f"Producto con ID {id} no encontrado.")

    # Elimina un producto del inventario
    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                self.guardar_inventario()
                print(f"Producto {producto.nombre} eliminado exitosamente.")
                return
        print(f"Producto con ID {id} no encontrado.")

    # Lista todos los productos en el inventario
    def listar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)

# Ejemplo de uso del sistema de inventario
if __name__ == "__main__":
    inventario = Inventario()

    # Añadir productos de prueba
    inventario.añadir_producto(Producto(1, 'Manzanas', 100, 0.5))
    inventario.añadir_producto(Producto(2, 'Peras', 50, 0.8))

    # Listar productos
    inventario.listar_productos()

    # Actualizar producto
    inventario.actualizar_producto(1, cantidad=120)

    # Eliminar producto
    inventario.eliminar_producto(2)

    # Listar productos después de las modificaciones
    inventario.listar_productos()

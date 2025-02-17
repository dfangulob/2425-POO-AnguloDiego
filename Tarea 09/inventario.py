from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        if not any(p.get_id() == id_producto for p in self.productos):
            nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
            self.productos.append(nuevo_producto)
            print(f"Producto '{nombre}' añadido exitosamente.")
        else:
            print("Error: El ID del producto ya existe.")

    def eliminar_producto(self, id_producto):
        producto_a_eliminar = next((p for p in self.productos if p.get_id() == id_producto), None)
        if producto_a_eliminar:
            self.productos.remove(producto_a_eliminar)
            print(f"Producto con ID {id_producto} eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = next((p for p in self.productos if p.get_id() == id_producto), None)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            print("Productos encontrados:")
            for producto in productos_encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if self.productos:
            print("Inventario actual:")
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")
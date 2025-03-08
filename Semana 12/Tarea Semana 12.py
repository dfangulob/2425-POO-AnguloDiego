###Sistema de gestion de biblioteca digital
##Constuimos una clase libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para almacenar el título y el autor, ya que son inmutables
##Se crea una tupla titulo de autor
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
##Cadena de texto (string)
    def __str__(self):
        return f"Libro: {self.titulo_autor[0]} por {self.titulo_autor[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

##Se define una clase llamada usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para almacenar los libros prestados al usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Definición de la clase Biblioteca
class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar libros disponibles, con ISBN como clave
        self.libros_disponibles = {}
        # Conjunto para almacenar IDs de usuarios únicos
        self.usuarios_registrados = set()
        # Diccionario para almacenar usuarios registrados, con ID como clave
        self.usuarios = {}

    def añadir_libro(self, libro):
        # Añade un libro a la biblioteca si no existe ya
        if libro.isbn in self.libros_disponibles:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' añadido correctamente.")

    def quitar_libro(self, isbn):
        # Elimina un libro de la biblioteca por su ISBN
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado correctamente.")
        else:
            print(f"No se encontró ningún libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        # Registra un nuevo usuario si no está ya registrado
        if usuario.id_usuario in self.usuarios_registrados:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")

    def dar_de_baja_usuario(self, id_usuario):
        # Da de baja a un usuario por su ID
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja correctamente.")
        else:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        # Presta un libro a un usuario si ambos están registrados y el libro está disponible
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return
        if isbn not in self.libros_disponibles:
            print(f"El libro con ISBN {isbn} no está disponible.")
            return

        libro = self.libros_disponibles[isbn]
        usuario = self.usuarios[id_usuario]
        usuario.libros_prestados.append(libro)
        del self.libros_disponibles[isbn]
        print(f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        # Devuelve un libro prestado por un usuario
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return

        usuario = self.usuarios[id_usuario]
        libro_a_devolver = None
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_a_devolver = libro
                break

        if libro_a_devolver:
            usuario.libros_prestados.remove(libro_a_devolver)
            self.libros_disponibles[isbn] = libro_a_devolver
            print(f"Libro '{libro_a_devolver.titulo_autor[0]}' devuelto por {usuario.nombre}.")
        else:
            print(f"El usuario {usuario.nombre} no tiene prestado el libro con ISBN {isbn}.")

    def buscar_libros_por_titulo(self, titulo):
        # Busca libros por título
        resultados = [libro for libro in self.libros_disponibles.values() if libro.titulo_autor[0] == titulo]
        return resultados

    def buscar_libros_por_autor(self, autor):
        # Busca libros por autor
        resultados = [libro for libro in self.libros_disponibles.values() if libro.titulo_autor[1] == autor]
        return resultados

    def buscar_libros_por_categoria(self, categoria):
        # Busca libros por categoría
        resultados = [libro for libro in self.libros_disponibles.values() if libro.categoria == categoria]
        return resultados

    def listar_libros_prestados(self, id_usuario):
        # Lista los libros prestados a un usuario
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return

        usuario = self.usuarios[id_usuario]
        if not usuario.libros_prestados:
            print(f"El usuario {usuario.nombre} no tiene libros prestados.")
        else:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)


# Pruebas del sistema
if __name__ == "__main__":
    # Crear algunos libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "978-0307474728")
    libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", "978-0451524935")
    libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "978-0156012195")

    # Crear una biblioteca
    biblioteca = Biblioteca()

    # Añadir libros a la biblioteca
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Registrar usuarios
    usuario1 = Usuario("Juan Pérez", 1)
    usuario2 = Usuario("Ana Gómez", 2)
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro(1, "978-0307474728")  # Prestar "Cien años de soledad" a Juan
    biblioteca.prestar_libro(2, "978-0451524935")  # Prestar "1984" a Ana

    # Listar libros prestados
    biblioteca.listar_libros_prestados(1)
    biblioteca.listar_libros_prestados(2)

    # Devolver libros
    biblioteca.devolver_libro(1, "978-0307474728")  # Juan devuelve "Cien años de soledad"

    # Buscar libros por categoría
    resultados = biblioteca.buscar_libros_por_categoria("Ciencia Ficción")
    print("\nLibros de Ciencia Ficción:")
    for libro in resultados:
        print(libro)

    # Dar de baja a un usuario
    biblioteca.dar_de_baja_usuario(2)


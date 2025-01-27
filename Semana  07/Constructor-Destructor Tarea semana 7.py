##Se crea un usuario

class Usuario:
    def __init__(self, nombre_usuario):
        """
        Constructor de la clase Usuario.
        Este método se ejecuta cuando se crea un nuevo objeto de la clase Usuario.
        Inicializa los atributos del objeto y realiza una acción de bienvenida.
        """
        self.nombre_usuario = nombre_usuario  # Asigna el nombre del usuario al atributo 'nombre_usuario'
        print(f"¡Bienvenido, {self.nombre_usuario}! La sesión ha sido iniciada.")

    def realizar_accion(self, accion):
        """
        Simula una acción realizada por el usuario.
        Este método imprime una acción que el usuario está llevando a cabo.
        """
        print(f"{self.nombre_usuario} está realizando la acción: {accion}")

    def __del__(self):
        """
        Destructor de la clase Usuario.
        Este método se ejecuta cuando el objeto de la clase Usuario se elimina o cuando el programa finaliza.
        Se utiliza para realizar alguna acción de limpieza, como cerrar sesiones o liberar recursos.
        """
        print(f"La sesión de {self.nombre_usuario} ha sido cerrada. ¡Hasta luego!")


# Uso de la clase Usuario
usuario1 = Usuario("Diego")  # Se crea un objeto de la clase Usuario, lo que llama al constructor (__init__)
usuario1.realizar_accion("Creando un nuevo documento")

# Crear un segundo usuario
usuario2 = Usuario("Ana")  # Se crea otro objeto de la clase Usuario
usuario2.realizar_accion("Subiendo archivos al servidor")

# Eliminar explícitamente los objetos, lo que llamará al destructor (__del__)
del usuario1  # El objeto 'usuario1' es eliminado, lo que invoca el destructor
del usuario2  # El objeto 'usuario2' también es eliminado

# Nota: Si no eliminamos explícitamente los objetos, Python ejecutará el destructor automáticamente al final
# cuando el programa termine, ya que Python maneja la recolección de basura.
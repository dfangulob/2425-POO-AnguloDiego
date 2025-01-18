# Clase base (superclase)
class General:
    def __init__(self, nombre):
        self.nombre = nombre       # Atributo público
        self.rango = "General"     # Atributo público
        self.__estrategias = []    # Atributo privado (encapsulación)

    # Método público
    def planificar(self, estrategia):
        self.__estrategias.append(estrategia)
        print(f"{self.rango} {self.nombre} ha anadido una nueva estrategia: {estrategia}")

    # Método público para mostrar estrategias
    def mostrar_estrategias(self):
        print(f"Estrategias del {self.rango} {self.nombre}: {', '.join(self.__estrategias) if self.__estrategias else 'Ninguna'}")

    # Método público que puede ser sobrescrito
    def reportar(self):
        print(f"{self.rango} {self.nombre}: La estrategia esta en marcha.")

# Clase derivada
class Sargento(General):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.rango = "Sargento"  # Cambia el rango

    # Sobrescritura de método (polimorfismo)
    def reportar(self):
        print(f"{self.rango} {self.nombre}: El pelotón está listo para el despliegue.")

# Otra clase derivada
class Militar(Sargento):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.rango = "Militar"  # Cambia el rango

    # Sobrescritura de método (polimorfismo)
    def reportar(self):
        print(f"{self.rango} {self.nombre}: ¡Preparado para seguir órdenes!")

# Bloque principal del programa
if __name__ == "__main__":
    # Crear una instancia de General
    general = General("María López")
    general.planificar("Defensa estratégica")
    general.planificar("Ataque coordinado")
    general.reportar()
    general.mostrar_estrategias()

    # Crear una instancia de Sargento
    sargento = Sargento("Luis Fernández")
    sargento.reportar()

    # Crear una instancia de Militar
    militar = Militar("Carlos Pérez")
    militar.reportar()

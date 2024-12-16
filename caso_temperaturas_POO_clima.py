class Clima:
    def __init__(self):
        self.temperaturas = []  # Lista para almacenar las temperaturas diarias
    
    def ingresar_temperaturas(self):
        for i in range(7):  # 7 días en la semana
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                    # Validar si la temperatura está dentro de un rango razonable
                    if temp < -50 or temp > 50:
                        print("La temperatura debe estar entre -50°C y 50°C.")
                    else:
                        self.temperaturas.append(temp)
                        break
                except ValueError:
                    print("Por favor, ingrese un número válido para la temperatura.")
    
    def calcular_promedio(self):
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio
    
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio de las temperaturas de la semana es: {promedio:.2f} grados.")

def main():
    print("Este programa calcula el promedio semanal de las temperaturas.")
    
    # Crear una instancia de la clase Clima
    clima = Clima()
    
    # Ingresar las temperaturas diarias
    clima.ingresar_temperaturas()
    
    # Mostrar el promedio semanal
    clima.mostrar_promedio()

# Ejecutar el programa
if __name__ == "__main__":
    main()
#Clase Clima:
#Solicita al usuario ingresar las temperaturas de la semana.
#calcular_promedio: Calcula el promedio de las temperaturas ingresadas.
# mostrar_promedio: Muestra el promedio de las temperaturas usando el método calcular_promedio.
#Función main:
# La función principal está organizada, crea una instancia de la clase Clima, solicita la entrada de datos y muestra el resultado.
#se agrega un campo a ingresar temperaturas válidas entre -50º y 50 º.

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # 7 días en la semana
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

# Función principal para ejecutar el programa
def main():
    print("Este programa calcula el promedio semanal de las temperaturas.")
    
    # Ingresar las temperaturas diarias
    temperaturas = ingresar_temperaturas()
    
    # Calcular y mostrar el promedio semanal
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio de las temperaturas de la semana es: {promedio:.2f} grados.")
    
# Ejecutar el programa
if __name__ == "__main__":
    main()

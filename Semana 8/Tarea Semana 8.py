import os
import subprocess


def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un script Python.

    :param ruta_script: Ruta del script a mostrar.
    :return: Contenido del script o None si hay un error.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    """
    Ejecuta un script Python en una nueva terminal.

    :param ruta_script: Ruta del script a ejecutar.
    """
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script], shell=True)
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


def obtener_archivos_o_carpetas(ruta_base):
    """
    Obtiene la lista de archivos o carpetas en la ruta base.

    :param ruta_base: Ruta base del proyecto.
    :return: Lista de archivos o carpetas.
    """
    try:
        elementos = [f.name for f in os.scandir(ruta_base) if f.is_dir() or f.is_file()]
        return elementos
    except FileNotFoundError:
        print(f"La ruta {ruta_base} no existe. Verifica la estructura de carpetas.")
        return []


def mostrar_menu():
    """
    Muestra el menú principal del dashboard.
    """
    # Define la ruta base del proyecto (ajusta esta ruta según tu estructura)
    ruta_base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Sube un nivel desde la carpeta actual

    # Obtener la lista de archivos o carpetas en la ruta base
    elementos = obtener_archivos_o_carpetas(ruta_base)

    if not elementos:
        print("No se encontraron archivos o carpetas en la ruta base.")
        return

    while True:
        print("\n=== Menú Principal - Dashboard ===")
        for i, elemento in enumerate(elementos, start=1):
            print(f"{i} - {elemento}")
        print("0 - Salir")

        eleccion = input("Elige un elemento o '0' para salir: ")
        if eleccion == '0':
            print("Saliendo del programa.")
            break
        else:
            try:
                eleccion = int(eleccion) - 1
                if 0 <= eleccion < len(elementos):
                    ruta_elemento = os.path.join(ruta_base, elementos[eleccion])
                    if os.path.isdir(ruta_elemento):
                        mostrar_sub_menu(ruta_elemento)
                    elif os.path.isfile(ruta_elemento) and ruta_elemento.endswith('.py'):
                        codigo = mostrar_codigo(ruta_elemento)
                        if codigo:
                            ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                            if ejecutar == '1':
                                ejecutar_codigo(ruta_elemento)
                            elif ejecutar == '0':
                                print("No se ejecutó el script.")
                            else:
                                print("Opción no válida. Regresando al menú principal.")
                            input("\nPresiona Enter para volver al menú principal.")
                    else:
                        print("El elemento seleccionado no es una carpeta ni un script Python.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")


def mostrar_sub_menu(ruta_elemento):
    """
    Muestra el submenú para seleccionar archivos dentro de una carpeta.

    :param ruta_elemento: Ruta de la carpeta seleccionada.
    """
    elementos = obtener_archivos_o_carpetas(ruta_elemento)

    if not elementos:
        print("No se encontraron archivos o carpetas en esta ruta.")
        return

    while True:
        print(f"\n=== Submenú - {os.path.basename(ruta_elemento)} ===")
        for i, elemento in enumerate(elementos, start=1):
            print(f"{i} - {elemento}")
        print("0 - Regresar al menú principal")

        eleccion = input("Elige un elemento o '0' para regresar: ")
        if eleccion == '0':
            break
        else:
            try:
                eleccion = int(eleccion) - 1
                if 0 <= eleccion < len(elementos):
                    ruta_seleccionada = os.path.join(ruta_elemento, elementos[eleccion])
                    if os.path.isdir(ruta_seleccionada):
                        mostrar_sub_menu(ruta_seleccionada)
                    elif os.path.isfile(ruta_seleccionada) and ruta_seleccionada.endswith('.py'):
                        codigo = mostrar_codigo(ruta_seleccionada)
                        if codigo:
                            ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                            if ejecutar == '1':
                                ejecutar_codigo(ruta_seleccionada)
                            elif ejecutar == '0':
                                print("No se ejecutó el script.")
                            else:
                                print("Opción no válida. Regresando al submenú.")
                            input("\nPresiona Enter para volver al submenú.")
                    else:
                        print("El elemento seleccionado no es una carpeta ni un script Python.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()




import tkinter as tk
from tkinter import messagebox

# Creamos la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")

# Lista para guardar tareas (cada elemento es un string)
tareas = []

# Función para actualizar la lista de tareas en pantalla
def actualizar_lista():
    lista_tareas.delete(0, tk.END)  # Borra todo lo que hay en la lista
    for tarea in tareas:
        lista_tareas.insert(tk.END, tarea)  # Inserta cada tarea en la lista visual

# Función para añadir una nueva tarea
def añadir_tarea(event=None):  # event=None permite que esta función se use con y sin teclado
    texto = entrada_tarea.get()
    if texto:
        tareas.append(texto)
        entrada_tarea.delete(0, tk.END)  # Borra el texto del Entry
        actualizar_lista()

# Función para marcar una tarea como completada
def completar_tarea(event=None):
    try:
        index = lista_tareas.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        tarea = tareas[index]
        if not tarea.startswith("[✓]"):
            tareas[index] = "[✓] " + tarea  # Añade marca de completado
            actualizar_lista()
    except IndexError:
        pass  # Si no hay ninguna tarea seleccionada, no hace nada

# Función para eliminar una tarea
def eliminar_tarea(event=None):
    try:
        index = lista_tareas.curselection()[0]
        tareas.pop(index)  # Elimina la tarea del listado
        actualizar_lista()
    except IndexError:
        pass

# Función para cerrar la aplicación con Escape
def cerrar_app(event=None):
    root.quit()

# Campo de entrada de texto para nuevas tareas
entrada_tarea = tk.Entry(root, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", añadir_tarea)  # Asocia tecla Enter a añadir_tarea()

# Botones para cada acción
btn_añadir = tk.Button(root, text="Añadir Tarea", command=añadir_tarea)
btn_añadir.pack(pady=5)

btn_completar = tk.Button(root, text="Marcar como Completada", command=completar_tarea)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Lista visual donde se muestran las tareas
lista_tareas = tk.Listbox(root, width=50, height=10)
lista_tareas.pack(pady=10)

# Asociamos los atajos de teclado a sus funciones
root.bind("<c>", completar_tarea)       # Letra c para completar
root.bind("<C>", completar_tarea)       # También mayúscula
root.bind("<d>", eliminar_tarea)        # Letra d para eliminar
root.bind("<D>", eliminar_tarea)        # También mayúscula
root.bind("<Escape>", cerrar_app)       # Escape para cerrar

# Inicia el bucle principal de la app
root.mainloop()

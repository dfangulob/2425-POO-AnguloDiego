import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica")

# Variables
data_list = []

# Función para agregar datos
def agregar_dato():
    dato = entry.get()  # Obtener el dato del campo de texto
    if dato:  # Si el dato no está vacío
        data_list.append(dato)
        update_lista()
        entry.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un dato.")

# Función para limpiar los datos
def limpiar_datos():
    entry.delete(0, tk.END)  # Limpiar el campo de texto
    listbox.delete(0, tk.END)  # Limpiar la lista
    data_list.clear()  # Limpiar la lista de datos

# Función para actualizar la lista mostrada
def update_lista():
    listbox.delete(0, tk.END)  # Limpiar la lista actual
    for item in data_list:
        listbox.insert(tk.END, item)  # Insertar los datos nuevos

# Crear los componentes de la interfaz
label = tk.Label(root, text="Ingresa un dato:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

btn_agregar = tk.Button(root, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

# Crear la lista para mostrar los datos
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_datos)
btn_limpiar.pack(pady=5)

# Ejecutar la interfaz
root.mainloop()

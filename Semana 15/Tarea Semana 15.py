import tkinter as tk
from tkinter import messagebox

# Función para agregar una nueva tarea a la lista
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)  # Inserta la tarea al final de la lista
        entry_task.delete(0, tk.END)  # Borra el campo de entrada después de agregar la tarea
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

# Función para marcar una tarea como completada
def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        task_text = listbox_tasks.get(selected_task_index)  # Obtiene el texto de la tarea seleccionada
        listbox_tasks.delete(selected_task_index)  # Elimina la tarea de la lista
        listbox_tasks.insert(selected_task_index, f"✔ {task_text}")  # Inserta la tarea marcada como completada
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")

# Función para eliminar una tarea de la lista
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        listbox_tasks.delete(selected_task_index)  # Elimina la tarea de la lista
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Función para añadir una tarea cuando se presiona la tecla Enter
def add_task_enter(event):
    add_task()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")  # Título de la ventana
root.geometry("400x400")  # Tamaño de la ventana

# Campo de entrada para escribir nuevas tareas
tk.Label(root, text="Nueva tarea:").pack(pady=5)
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)
entry_task.bind("<Return>", add_task_enter)  # Asigna la función de agregar tarea al presionar Enter

# Botones de la interfaz gráfica
tk.Button(root, text="Añadir Tarea", command=add_task).pack(pady=5)
tk.Button(root, text="Marcar como Completada", command=mark_completed).pack(pady=5)
tk.Button(root, text="Eliminar Tarea", command=delete_task).pack(pady=5)

# Lista donde se mostrarán las tareas
listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()


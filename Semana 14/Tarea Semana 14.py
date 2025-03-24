##se realizara una agenda
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


# Clase principal de la aplicación de agenda
class AgendaApp:
    def __init__(self, root):
        # Inicializa la ventana principal y establece título y tamaño
        self.root = root
        self.root.title("Agenda Personal")  # Título de la ventana
        self.root.geometry("500x400")  # Tamaño de la ventana

        # Frame para la entrada de datos (fecha, hora, descripción)
        frame_input = ttk.Frame(root, padding=10)
        frame_input.pack(fill='x')  # Ajustar el frame al ancho de la ventana

        # Etiqueta y campo de entrada para la fecha del evento
        ttk.Label(frame_input, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(frame_input, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada para la hora del evento
        ttk.Label(frame_input, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = ttk.Entry(frame_input, width=10)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada para la descripción del evento
        ttk.Label(frame_input, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = ttk.Entry(frame_input, width=30)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botón para agregar un evento a la lista
        self.add_button = ttk.Button(frame_input, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Treeview para mostrar la lista de eventos
        self.tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")  # Encabezado de columna Fecha
        self.tree.heading("Hora", text="Hora")  # Encabezado de columna Hora
        self.tree.heading("Descripción", text="Descripción")  # Encabezado de columna Descripción
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)  # Agregar treeview a la ventana

        # Botón para eliminar un evento seleccionado de la lista
        self.delete_button = ttk.Button(root, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.delete_button.pack(pady=5)  # Agregar botón a la ventana

        # Botón para salir de la aplicación
        self.exit_button = ttk.Button(root, text="Salir", command=root.quit)
        self.exit_button.pack(pady=5)  # Agregar botón de salir a la ventana

    # Método para agregar un evento a la lista
    def add_event(self):
        fecha = self.date_entry.get()  # Obtener fecha del campo de entrada
        hora = self.time_entry.get()  # Obtener hora del campo de entrada
        descripcion = self.desc_entry.get()  # Obtener descripción del campo de entrada

        # Verificar que todos los campos estén completos antes de agregar el evento
        if fecha and hora and descripcion:
            # Insertar los valores en el Treeview
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            # Limpiar los campos de entrada después de agregar el evento
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            # Mostrar un mensaje de advertencia si falta algún campo
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

    # Método para eliminar el evento seleccionado
    def delete_event(self):
        selected_item = self.tree.selection()  # Obtener el evento seleccionado
        if selected_item:
            # Mostrar un cuadro de confirmación antes de eliminar el evento
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este evento?")
            if confirm:
                # Eliminar el evento de la lista si se confirma
                self.tree.delete(selected_item)
        else:
            # Mostrar un mensaje si no se selecciona ningún evento
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")


# Código principal para iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = AgendaApp(root)  # Crear la instancia de la aplicación
    root.mainloop()  # Iniciar el bucle de eventos de Tkinter

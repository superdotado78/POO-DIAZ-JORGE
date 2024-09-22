import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para agregar un evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_desc.get()

    if fecha and hora and descripcion:
        tree.insert('', 'end', values=(fecha, hora, descripcion))
        entry_fecha.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, rellene todos los campos")

# Función para eliminar el evento seleccionado
def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Eliminar evento", "Seleccione un evento para eliminar")

# Función para salir de la aplicación
def salir():
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")

# Frame para la lista de eventos (TreeView)
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Frame para los campos de entrada
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Fecha (DD/MM/AAAA):").grid(row=0, column=0)
entry_fecha = tk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1)

tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
entry_desc = tk.Entry(frame_entrada)
entry_desc.grid(row=2, column=1)

# Frame para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=10)

# Iniciar la aplicación
root.mainloop()

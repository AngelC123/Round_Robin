import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo Round Robin")

        # Entradas para el número de procesos
        self.frame_procesos = tk.Frame(root)
        self.frame_procesos.pack(pady=10)

        tk.Label(self.frame_procesos, text="Número de procesos:").grid(row=0, column=0)
        self.entry_num_procesos = tk.Entry(self.frame_procesos)
        self.entry_num_procesos.grid(row=0, column=1)

        tk.Label(self.frame_procesos, text="Quantum:").grid(row=1, column=0)
        self.entry_quantum = tk.Entry(self.frame_procesos)
        self.entry_quantum.grid(row=1, column=1)

        self.entry_nombres = []
        self.entry_rafagas = []
        self.entry_llegadas = []

        tk.Button(self.frame_procesos, text="Crear Campos", command=self.crear_campos_procesos).grid(row=2, column=2, columnspan=2)

        # Botón para ejecutar el algoritmo
        self.boton_ejecutar = tk.Button(root, text="Ejecutar Algoritmo", command=None)
        self.boton_ejecutar.pack(pady=10)

        # Frame para la gráfica
        self.frame_grafica = tk.Frame(root)
        self.frame_grafica.pack()

    def crear_campos_procesos(self):
        n = int(self.entry_num_procesos.get())
        for widget in self.frame_procesos.winfo_children()[3:]:
            widget.destroy()  # Limpiar campos existentes, pero no el quantum
        for i in range(n):
            tk.Label(self.frame_procesos, text=f"Nombre P{i+1}:").grid(row=i+2, column=0)
            entry_nombre = tk.Entry(self.frame_procesos)
            entry_nombre.grid(row=i+2, column=1)
            self.entry_nombres.append(entry_nombre)

            tk.Label(self.frame_procesos, text=f"Ráfaga P{i+1}:").grid(row=i+2, column=2)
            entry_rafaga = tk.Entry(self.frame_procesos)
            entry_rafaga.grid(row=i+2, column=3)
            self.entry_rafagas.append(entry_rafaga)

            tk.Label(self.frame_procesos, text=f"Llegada P{i+1}:").grid(row=i+2, column=4)
            entry_llegada = tk.Entry(self.frame_procesos)
            entry_llegada.grid(row=i+2, column=5)
            self.entry_llegadas.append(entry_llegada)

        # Asegúrate de que el campo del quantum no se elimine
        tk.Label(self.frame_procesos, text="Quantum:").grid(row=1, column=0)
        self.entry_quantum.grid(row=1, column=1)

    def mostrar_grafica(self, tiempos_espera, tiempos_procesamiento):
        figura = Figure(figsize=(5, 4), dpi=100)
        grafico = figura.add_subplot(111)

        n = len(tiempos_espera)
        indices = range(n)
        bar_width = 0.35

        grafico.bar(indices, tiempos_espera, bar_width, color='red', label='Tiempo de Espera')
        grafico.bar([i + bar_width for i in indices], tiempos_procesamiento, bar_width, color='green', label='Tiempo de Procesamiento')

        grafico.set_xlabel('Procesos')
        grafico.set_ylabel('Tiempo')
        grafico.set_title('Algoritmo Round Robin')
        grafico.set_xticks([i + bar_width / 2 for i in indices])
        grafico.set_xticklabels([f'P{i+1}' for i in range(n)])
        grafico.legend()

        canvas = FigureCanvasTkAgg(figura, master=self.frame_grafica)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

    def mostrar_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo Round Robin")

        # Estilo
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12))

        # Entradas para el número de procesos y quantum
        self.frame_procesos = ttk.Frame(root, padding="10")
        self.frame_procesos.pack(pady=10)

        ttk.Label(self.frame_procesos, text="Número de procesos:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_num_procesos = ttk.Entry(self.frame_procesos)
        self.entry_num_procesos.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_procesos, text="Quantum:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_quantum = ttk.Entry(self.frame_procesos)
        self.entry_quantum.grid(row=1, column=1, padx=5, pady=5)

        self.entry_nombres = []
        self.entry_rafagas = []
        self.entry_llegadas = []

        ttk.Button(self.frame_procesos, text="Crear Campos", command=self.crear_campos_procesos).grid(row=2, column=0,
                                                                                                      columnspan=2,
                                                                                                      pady=10)

        # Botón para ejecutar el algoritmo
        self.boton_ejecutar = ttk.Button(root, text="Ejecutar Algoritmo", command=None)
        self.boton_ejecutar.pack(pady=10)

        # Frame para la gráfica
        self.frame_grafica = ttk.Frame(root, padding="10")
        self.frame_grafica.pack()

    def crear_campos_procesos(self):
        n = int(self.entry_num_procesos.get())

        # Guardar el valor actual del quantum
        quantum_valor = self.entry_quantum.get()

        # Limpiar campos existentes, pero no el quantum ni el número de procesos
        for widget in self.frame_procesos.winfo_children():
            if widget not in [self.entry_num_procesos, self.entry_quantum,
                              self.frame_procesos.grid_slaves(row=0, column=0)[0],
                              self.frame_procesos.grid_slaves(row=1, column=0)[0]]:
                widget.destroy()

        self.entry_nombres = []
        self.entry_rafagas = []
        self.entry_llegadas = []

        for i in range(n):
            ttk.Label(self.frame_procesos, text=f"Nombre P{i + 1}:").grid(row=i + 2, column=0, padx=5, pady=5)
            entry_nombre = ttk.Entry(self.frame_procesos)
            entry_nombre.grid(row=i + 2, column=1, padx=5, pady=5)
            self.entry_nombres.append(entry_nombre)

            ttk.Label(self.frame_procesos, text=f"Ráfaga P{i + 1}:").grid(row=i + 2, column=2, padx=5, pady=5)
            entry_rafaga = ttk.Entry(self.frame_procesos)
            entry_rafaga.grid(row=i + 2, column=3, padx=5, pady=5)
            self.entry_rafagas.append(entry_rafaga)

            ttk.Label(self.frame_procesos, text=f"Llegada P{i + 1}:").grid(row=i + 2, column=4, padx=5, pady=5)
            entry_llegada = ttk.Entry(self.frame_procesos)
            entry_llegada.grid(row=i + 2, column=5, padx=5, pady=5)
            self.entry_llegadas.append(entry_llegada)

        # Restaurar el valor del quantum
        self.entry_quantum.delete(0, tk.END)
        self.entry_quantum.insert(0, quantum_valor)

    def mostrar_grafica(self, tiempos_espera, tiempos_procesamiento):
        figura = Figure(figsize=(5, 4), dpi=100)
        grafico = figura.add_subplot(111)

        n = len(tiempos_espera)
        indices = range(n)
        bar_width = 0.35

        # Cambiar la orientación de la gráfica
        grafico.barh(indices, tiempos_espera, bar_width, color='red', label='Tiempo de Espera')
        grafico.barh([i + bar_width for i in indices], tiempos_procesamiento, bar_width, color='green',
                     label='Tiempo de Procesamiento')

        grafico.set_ylabel('Procesos')
        grafico.set_xlabel('Tiempo')
        grafico.set_title('Resultados del Algoritmo Round Robin')
        grafico.set_yticks([i + bar_width / 2 for i in indices])
        grafico.set_yticklabels([f'P{i + 1}' for i in range(n)])
        grafico.legend()

        canvas = FigureCanvasTkAgg(figura, master=self.frame_grafica)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

    def mostrar_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

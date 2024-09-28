from modelo import Proceso, round_robin

class Controlador:
    def __init__(self, vista):
        self.vista = vista
        self.vista.boton_ejecutar.config(command=self.ejecutar_algoritmo)

    def ejecutar_algoritmo(self):
        try:
            n = int(self.vista.entry_num_procesos.get())
            procesos = []

            for i in range(n):
                nombre = self.vista.entry_nombres[i].get()
                rafaga = int(self.vista.entry_rafagas[i].get())
                llegada = int(self.vista.entry_llegadas[i].get())
                procesos.append(Proceso(nombre, rafaga, llegada))

            quantum = int(self.vista.entry_quantum.get())

            tiempos_espera, tiempos_procesamiento = round_robin(procesos, quantum)

            self.vista.mostrar_grafica(tiempos_espera, tiempos_procesamiento)

        except ValueError:
            self.vista.mostrar_error("Por favor, ingrese valores válidos.")

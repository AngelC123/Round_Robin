class Proceso:
    def __init__(self, nombre, rafaga, llegada):
        self.nombre = nombre
        self.rafaga = rafaga
        self.llegada = llegada
        self.tiempo_espera = 0
        self.tiempo_procesamiento = 0

def round_robin(procesos, quantum):
    tiempo_actual = 0
    cola = []
    tiempos_espera = []
    tiempos_procesamiento = []

    while procesos or cola:
        while procesos and procesos[0].llegada <= tiempo_actual:
            cola.append(procesos.pop(0))

        if cola:
            proceso = cola.pop(0)
            tiempo_a_procesar = min(proceso.rafaga, quantum)
            proceso.rafaga -= tiempo_a_procesar
            proceso.tiempo_procesamiento += tiempo_a_procesar
            tiempo_actual += tiempo_a_procesar

            if proceso.rafaga > 0:
                cola.append(proceso)
            else:
                proceso.tiempo_espera = tiempo_actual - proceso.tiempo_procesamiento - proceso.llegada
                tiempos_espera.append(proceso.tiempo_espera)
                tiempos_procesamiento.append(proceso.tiempo_procesamiento)
        else:
            tiempo_actual += 1  # Esperar si no hay procesos listos

    return tiempos_espera, tiempos_procesamiento
import random
import time
from threading import Thread, Lock

class Proceso:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
        self.mutex = Lock()

def ejecutar_proceso(proceso):
    with proceso.mutex:
        print(f"Proceso {proceso.nombre} iniciado")
        tiempo_demora = random.uniform(1, 5)
        time.sleep(tiempo_demora)
        print(f"Proceso {proceso.nombre} terminado ({tiempo_demora:.2f} segundos)")

def interrumpir(proceso1, proceso2):
    print(f"Proceso {proceso1.nombre} interrumpió a Proceso {proceso2.nombre}")

def main():
    resta = Proceso("Resta", 1)
    suma = Proceso("Suma", 2)
    division = Proceso("Division", 3)
    multiplicacion = Proceso("Multiplicacion", 4)

    procesos = [resta, suma, division, multiplicacion]

    while True:
        proceso1, proceso2 = random.sample(procesos, 2)
        if proceso1.valor > proceso2.valor:
            hilo_proceso1 = Thread(target=ejecutar_proceso, args=(proceso1,))
            hilo_proceso2 = Thread(target=ejecutar_proceso, args=(proceso2,))

            hilo_proceso1.start()
            time.sleep(0.5)
            hilo_proceso2.start()

            hilo_proceso1.join()
            hilo_proceso2.join()

            interrumpir(proceso1, proceso2)

if __name__ == "__main__":
    main()

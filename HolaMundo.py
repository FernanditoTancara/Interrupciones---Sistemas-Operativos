import time
import random
from threading import Thread

#Querarquia de Prioridades
#1: Multiplicacion
#2: Division
#3: Suma
#4 Resta

def resta():
    print("Resta iniciada")
    time.sleep(random.uniform(0, 10))
    print("Resta terminada")
def suma():
    print("Suma iniciada")
    time.sleep(random.uniform(0, 10))
    print("Suma terminada")
def division():
    print("División iniciada")
    time.sleep(random.uniform(0, 10))
    print("División terminada")
def multiplicacion():
    print("Multiplicación iniciada")
    time.sleep(random.uniform(0, 10))
    print("Multiplicación terminada")


def ejecutar_proceso(proceso, prioridad):
    start_time = time.time()
    print(f"{proceso.__name__} iniciada (Prioridad: {prioridad})")
    while time.time() - start_time < 5:
        if random.random() < 0.1:  # Generar interrupción con 10% de probabilidad
            interrumpir_otro_proceso(proceso.__name__, prioridad)
            break
        time.sleep(0.1)
    print(f"{proceso.__name__} terminada")

def interrumpir_otro_proceso(proceso_actual, prioridad_actual):
    procesos = [(resta, 1), (suma, 2), (division, 3), (multiplicacion, 4)]
    procesos = [p for p in procesos if p[1] < prioridad_actual]  # Filtrar por prioridad menor
    if procesos:
        proceso_a_interrumpir, _ = random.choice(procesos)
        print(f"{proceso_actual} interrumpió a {proceso_a_interrumpir}")
        Thread(target=proceso_a_interrumpir).start()
    else:
        print(f"No hay procesos de menor prioridad para interrumpir la {proceso_actual}")

Thread(target=ejecutar_proceso, args=(resta, 1)).start()
Thread(target=ejecutar_proceso, args=(suma, 2)).start()
Thread(target=ejecutar_proceso, args=(division, 3)).start()
Thread(target=ejecutar_proceso, args=(multiplicacion, 4)).start()

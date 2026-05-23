"""Patrón Facade: Proporciona una interfaz simplificada a un subsistema complejo."""


class CPU:
    def iniciar(self):
        return "CPU iniciada"


class Memoria:
    def cargar(self):
        return "Memoria cargada"


class DiscoDuro:
    def leer(self):
        return "Disco leído"


class ComputadoraFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memoria = Memoria()
        self.disco = DiscoDuro()

    def encender(self):
        resultados = [
            self.cpu.iniciar(),
            self.memoria.cargar(),
            self.disco.leer(),
        ]
        return "Computadora lista: " + " | ".join(resultados)


# Uso
pc = ComputadoraFacade()
print(pc.encender())

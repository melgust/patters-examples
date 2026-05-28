"""L - Liskov Substitution Principle (Principio de Sustitución de Liskov)

Las subclases deben poder sustituir a sus clases base sin romper el programa.
"""

from abc import ABC, abstractmethod


# MAL: Pingüino hereda de Ave pero no puede volar
class AveMal:
    def volar(self):
        return "Volando"


class PinguinoMal(AveMal):
    def volar(self):
        raise Exception("Los pingüinos no vuelan!")  # Rompe el contrato


# BIEN: Separar comportamientos en interfaces adecuadas
class Ave(ABC):
    @abstractmethod
    def mover(self) -> str:
        pass


class AveVoladora(Ave):
    def mover(self):
        return "Volando por el cielo"


class AveNoVoladora(Ave):
    def mover(self):
        return "Caminando por el suelo"


class Aguila(AveVoladora):
    pass


class Pinguino(AveNoVoladora):
    pass


# Uso: cualquier Ave puede usarse sin sorpresas
def hacer_mover(ave: Ave):
    print(ave.mover())


hacer_mover(Aguila())
hacer_mover(Pinguino())

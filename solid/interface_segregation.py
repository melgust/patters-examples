"""I - Interface Segregation Principle (Principio de Segregación de Interfaces)

Los clientes no deben depender de interfaces que no usan.
"""

from abc import ABC, abstractmethod


# MAL: Interfaz gorda que obliga a implementar métodos innecesarios
class TrabajadorMal(ABC):
    @abstractmethod
    def trabajar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def dormir(self):
        pass


class RobotMal(TrabajadorMal):
    def trabajar(self):
        return "Trabajando"

    def comer(self):
        pass  # Un robot no come, pero está obligado a implementarlo

    def dormir(self):
        pass  # Un robot no duerme


# BIEN: Interfaces pequeñas y específicas
class Trabajable(ABC):
    @abstractmethod
    def trabajar(self) -> str:
        pass


class Alimentable(ABC):
    @abstractmethod
    def comer(self) -> str:
        pass


class Humano(Trabajable, Alimentable):
    def trabajar(self):
        return "Humano trabajando"

    def comer(self):
        return "Humano comiendo"


class Robot(Trabajable):
    def trabajar(self):
        return "Robot trabajando"


# Uso
print(Humano().trabajar())
print(Humano().comer())
print(Robot().trabajar())  # Robot solo implementa lo que necesita

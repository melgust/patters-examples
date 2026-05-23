"""Patrón Factory Method: Delega la creación de objetos a subclases."""

from abc import ABC, abstractmethod


class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass


class Camion(Transporte):
    def entregar(self):
        return "Entrega por tierra en camión"


class Barco(Transporte):
    def entregar(self):
        return "Entrega por mar en barco"


class Logistica(ABC):
    @abstractmethod
    def crear_transporte(self) -> Transporte:
        pass

    def planificar(self):
        transporte = self.crear_transporte()
        return transporte.entregar()


class LogisticaTerrestre(Logistica):
    def crear_transporte(self):
        return Camion()


class LogisticaMaritima(Logistica):
    def crear_transporte(self):
        return Barco()


# Uso
for logistica in [LogisticaTerrestre(), LogisticaMaritima()]:
    print(logistica.planificar())

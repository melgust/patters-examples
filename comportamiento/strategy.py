"""Patrón Strategy: Permite intercambiar algoritmos en tiempo de ejecución."""

from abc import ABC, abstractmethod


class EstrategiaPago(ABC):
    @abstractmethod
    def pagar(self, monto: float) -> str:
        pass


class PagoTarjeta(EstrategiaPago):
    def pagar(self, monto):
        return f"Pagado ${monto} con tarjeta"


class PagoPayPal(EstrategiaPago):
    def pagar(self, monto):
        return f"Pagado ${monto} con PayPal"


class PagoCripto(EstrategiaPago):
    def pagar(self, monto):
        return f"Pagado ${monto} con criptomoneda"


class Carrito:
    def __init__(self, estrategia: EstrategiaPago):
        self._estrategia = estrategia

    def checkout(self, monto):
        return self._estrategia.pagar(monto)


# Uso
for metodo in [PagoTarjeta(), PagoPayPal(), PagoCripto()]:
    carrito = Carrito(metodo)
    print(carrito.checkout(100.0))

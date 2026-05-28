"""O - Open/Closed Principle (Principio Abierto/Cerrado)

Las clases deben estar abiertas para extensión pero cerradas para modificación.
"""

from abc import ABC, abstractmethod


# MAL: Hay que modificar la clase cada vez que se agrega un descuento
class CalculadoraDescuentoMal:
    def calcular(self, tipo: str, precio: float):
        if tipo == "estudiante":
            return precio * 0.8
        elif tipo == "empleado":
            return precio * 0.7
        # Cada nuevo tipo requiere modificar esta clase


# BIEN: Se extiende creando nuevas clases sin tocar las existentes
class Descuento(ABC):
    @abstractmethod
    def aplicar(self, precio: float) -> float:
        pass


class DescuentoEstudiante(Descuento):
    def aplicar(self, precio):
        return precio * 0.8


class DescuentoEmpleado(Descuento):
    def aplicar(self, precio):
        return precio * 0.7


class DescuentoVIP(Descuento):
    def aplicar(self, precio):
        return precio * 0.5


class Calculadora:
    def calcular(self, descuento: Descuento, precio: float):
        return descuento.aplicar(precio)


# Uso: agregar nuevos descuentos sin modificar Calculadora
calc = Calculadora()
print(f"Estudiante: ${calc.calcular(DescuentoEstudiante(), 100)}")
print(f"VIP: ${calc.calcular(DescuentoVIP(), 100)}")

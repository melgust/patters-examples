"""Patrón Decorator: Añade funcionalidad a objetos dinámicamente."""

from abc import ABC, abstractmethod


class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass


class NotificadorBase(Notificador):
    def enviar(self, mensaje):
        return f"Email: {mensaje}"


class DecoradorSMS(Notificador):
    def __init__(self, notificador: Notificador):
        self._notificador = notificador

    def enviar(self, mensaje):
        return f"{self._notificador.enviar(mensaje)} + SMS: {mensaje}"


class DecoradorSlack(Notificador):
    def __init__(self, notificador: Notificador):
        self._notificador = notificador

    def enviar(self, mensaje):
        return f"{self._notificador.enviar(mensaje)} + Slack: {mensaje}"


# Uso
notificador = DecoradorSlack(DecoradorSMS(NotificadorBase()))
print(notificador.enviar("Alerta!"))

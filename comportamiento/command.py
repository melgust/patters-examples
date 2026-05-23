"""Patrón Command: Encapsula una solicitud como un objeto."""

from abc import ABC, abstractmethod


class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def deshacer(self):
        pass


class Editor:
    def __init__(self):
        self.texto = ""


class ComandoEscribir(Comando):
    def __init__(self, editor: Editor, texto: str):
        self.editor = editor
        self.texto = texto

    def ejecutar(self):
        self.editor.texto += self.texto

    def deshacer(self):
        self.editor.texto = self.editor.texto[:-len(self.texto)]


class Historial:
    def __init__(self):
        self._comandos = []

    def ejecutar(self, comando: Comando):
        comando.ejecutar()
        self._comandos.append(comando)

    def deshacer(self):
        if self._comandos:
            self._comandos.pop().deshacer()


# Uso
editor = Editor()
historial = Historial()

historial.ejecutar(ComandoEscribir(editor, "Hola "))
historial.ejecutar(ComandoEscribir(editor, "Mundo"))
print(f"Texto: '{editor.texto}'")

historial.deshacer()
print(f"Después de deshacer: '{editor.texto}'")

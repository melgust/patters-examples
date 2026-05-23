"""Patrón Observer: Notifica cambios de estado a múltiples objetos."""


class Evento:
    def __init__(self):
        self._suscriptores = []

    def suscribir(self, fn):
        self._suscriptores.append(fn)

    def emitir(self, datos):
        for fn in self._suscriptores:
            fn(datos)


class Tienda:
    def __init__(self):
        self.evento_nuevo_producto = Evento()

    def agregar_producto(self, nombre):
        print(f"Nuevo producto: {nombre}")
        self.evento_nuevo_producto.emitir(nombre)


# Uso
tienda = Tienda()
tienda.evento_nuevo_producto.suscribir(lambda p: print(f"  [Email] {p} disponible!"))
tienda.evento_nuevo_producto.suscribir(lambda p: print(f"  [App] {p} en stock!"))
tienda.agregar_producto("Laptop")

"""D - Dependency Inversion Principle (Principio de Inversión de Dependencias)

Los módulos de alto nivel no deben depender de módulos de bajo nivel.
Ambos deben depender de abstracciones.
"""

from abc import ABC, abstractmethod


# MAL: La clase de alto nivel depende directamente de la implementación
class MySQLDatabase:
    def conectar(self):
        return "Conectado a MySQL"


class AppMal:
    def __init__(self):
        self.db = MySQLDatabase()  # Acoplamiento directo

    def iniciar(self):
        return self.db.conectar()


# BIEN: Depender de abstracciones
class Database(ABC):
    @abstractmethod
    def conectar(self) -> str:
        pass


class MySQL(Database):
    def conectar(self):
        return "Conectado a MySQL"


class PostgreSQL(Database):
    def conectar(self):
        return "Conectado a PostgreSQL"


class MongoDB(Database):
    def conectar(self):
        return "Conectado a MongoDB"


class App:
    def __init__(self, db: Database):
        self.db = db  # Depende de la abstracción

    def iniciar(self):
        return self.db.conectar()


# Uso: se puede cambiar la DB sin modificar App
print(App(MySQL()).iniciar())
print(App(PostgreSQL()).iniciar())
print(App(MongoDB()).iniciar())

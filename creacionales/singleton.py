"""Patrón Singleton: Garantiza que una clase tenga una única instancia."""


class Singleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia


# Uso
s1 = Singleton()
s2 = Singleton()
print(f"s1 is s2: {s1 is s2}")  # True

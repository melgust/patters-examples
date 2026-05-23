"""Patrón Builder: Construye objetos complejos paso a paso."""


class Pizza:
    def __init__(self):
        self.ingredientes = []

    def __str__(self):
        return f"Pizza con: {', '.join(self.ingredientes)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def agregar_masa(self, tipo):
        self.pizza.ingredientes.append(f"masa {tipo}")
        return self

    def agregar_salsa(self, tipo):
        self.pizza.ingredientes.append(f"salsa {tipo}")
        return self

    def agregar_topping(self, topping):
        self.pizza.ingredientes.append(topping)
        return self

    def construir(self):
        return self.pizza


# Uso
pizza = (PizzaBuilder()
         .agregar_masa("delgada")
         .agregar_salsa("tomate")
         .agregar_topping("queso")
         .agregar_topping("champiñones")
         .construir())

print(pizza)

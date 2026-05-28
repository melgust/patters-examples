"""S - Single Responsibility Principle (Principio de Responsabilidad Única)

Cada clase debe tener una sola razón para cambiar.
"""


# MAL: Una clase hace todo
class EmpleadoMal:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self):
        return self.salario

    def guardar_en_db(self):
        print(f"Guardando {self.nombre} en base de datos")

    def generar_reporte(self):
        print(f"Reporte de {self.nombre}: ${self.salario}")


# BIEN: Cada clase tiene una sola responsabilidad
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self):
        return self.salario


class EmpleadoRepositorio:
    def guardar(self, empleado: Empleado):
        print(f"Guardando {empleado.nombre} en base de datos")


class EmpleadoReporte:
    def generar(self, empleado: Empleado):
        print(f"Reporte de {empleado.nombre}: ${empleado.salario}")


# Uso
emp = Empleado("Ana", 5000)
EmpleadoRepositorio().guardar(emp)
EmpleadoReporte().generar(emp)

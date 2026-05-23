"""Patrón Adapter: Permite que interfaces incompatibles trabajen juntas."""


class SistemaViejo:
    def obtener_datos_xml(self):
        return "<datos><nombre>producto</nombre></datos>"


class SistemaModerno:
    def procesar_json(self, datos: dict):
        return f"Procesado: {datos}"


class Adaptador:
    def __init__(self, sistema_viejo: SistemaViejo, sistema_moderno: SistemaModerno):
        self.viejo = sistema_viejo
        self.moderno = sistema_moderno

    def procesar(self):
        xml = self.viejo.obtener_datos_xml()
        # Simulación de conversión XML -> dict
        datos = {"nombre": "producto", "origen": xml}
        return self.moderno.procesar_json(datos)


# Uso
adaptador = Adaptador(SistemaViejo(), SistemaModerno())
print(adaptador.procesar())

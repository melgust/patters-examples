# Patrones de Diseño en Python

## Creacionales

Estos patrones se enfocan en **cómo se crean los objetos**, abstrayendo el proceso de instanciación.

---

### Singleton

**¿Cuándo usarlo?**
- Cuando necesitas exactamente una instancia de una clase en toda la aplicación.
- Ejemplos: conexión a base de datos, logger, configuración global, pool de conexiones.

**¿Cómo funciona?**
Sobrescribe el método `__new__` para verificar si ya existe una instancia. Si existe, retorna la misma; si no, crea una nueva y la almacena como atributo de clase.

```python
s1 = Singleton()
s2 = Singleton()
# s1 y s2 son el mismo objeto en memoria
```

---

### Factory Method

**¿Cuándo usarlo?**
- Cuando no sabes de antemano qué tipo exacto de objeto necesitas crear.
- Cuando quieres que las subclases decidan qué clase instanciar.
- Ejemplos: crear diferentes tipos de documentos, transportes, notificaciones según el contexto.

**¿Cómo funciona?**
Define una interfaz para crear objetos, pero deja que las subclases decidan qué clase concreta instanciar. El código cliente trabaja con la interfaz abstracta sin conocer la implementación específica.

```python
logistica = LogisticaTerrestre()  # Crea Camion internamente
logistica.planificar()             # Usa el transporte sin saber cuál es
```

---

### Builder

**¿Cuándo usarlo?**
- Cuando un objeto tiene muchos parámetros opcionales o configuraciones.
- Cuando quieres construir diferentes representaciones del mismo objeto.
- Ejemplos: construir consultas SQL, configurar objetos complejos como reportes, menús, o formularios.

**¿Cómo funciona?**
Separa la construcción de un objeto complejo de su representación. Usa una interfaz fluida (métodos encadenados con `return self`) para ir agregando partes paso a paso, y al final llama a `construir()` para obtener el objeto final.

```python
pizza = (PizzaBuilder()
         .agregar_masa("delgada")
         .agregar_salsa("tomate")
         .agregar_topping("queso")
         .construir())
```

---

## Estructurales

Estos patrones se enfocan en **cómo se componen los objetos** para formar estructuras más grandes.

---

### Adapter

**¿Cuándo usarlo?**
- Cuando necesitas integrar una clase existente cuya interfaz no es compatible con el resto del sistema.
- Cuando trabajas con código legado o librerías de terceros.
- Ejemplos: integrar APIs externas, conectar sistemas viejos con nuevos, convertir formatos de datos.

**¿Cómo funciona?**
Crea una clase intermedia (el adaptador) que traduce la interfaz de una clase a otra interfaz que el cliente espera. El adaptador envuelve al objeto incompatible y expone los métodos que el sistema necesita.

```python
adaptador = Adaptador(SistemaViejo(), SistemaModerno())
adaptador.procesar()  # Convierte XML del sistema viejo a JSON del moderno
```

---

### Decorator

**¿Cuándo usarlo?**
- Cuando quieres añadir responsabilidades a objetos individuales sin afectar a otros objetos de la misma clase.
- Cuando la herencia no es práctica porque generaría demasiadas subclases.
- Ejemplos: agregar logging, cifrado, compresión, o canales de notificación de forma combinable.

**¿Cómo funciona?**
Envuelve un objeto dentro de otro que implementa la misma interfaz. Cada decorador añade su comportamiento y delega al objeto envuelto. Se pueden apilar múltiples decoradores.

```python
# Notificador base + SMS + Slack, todo combinado
notificador = DecoradorSlack(DecoradorSMS(NotificadorBase()))
notificador.enviar("Alerta!")
```

---

### Facade

**¿Cuándo usarlo?**
- Cuando un subsistema es complejo y quieres ofrecer una interfaz simple al cliente.
- Cuando quieres desacoplar el código cliente de las dependencias internas.
- Ejemplos: inicializar un sistema con múltiples componentes, simplificar el uso de librerías complejas, orquestar servicios.

**¿Cómo funciona?**
Crea una clase que encapsula la interacción con múltiples objetos del subsistema. El cliente solo interactúa con la fachada, que internamente coordina las llamadas necesarias.

```python
pc = ComputadoraFacade()
pc.encender()  # Internamente inicia CPU, carga memoria y lee disco
```

---

## Comportamiento

Estos patrones se enfocan en **cómo se comunican los objetos** y cómo se distribuyen las responsabilidades.

---

### Strategy

**¿Cuándo usarlo?**
- Cuando tienes múltiples algoritmos para una tarea y quieres intercambiarlos en tiempo de ejecución.
- Cuando quieres evitar condicionales largos (`if/elif/else`) para seleccionar comportamiento.
- Ejemplos: métodos de pago, algoritmos de ordenamiento, estrategias de validación, cálculo de impuestos.

**¿Cómo funciona?**
Define una familia de algoritmos, encapsula cada uno en su propia clase con una interfaz común, y permite que el cliente elija cuál usar. El contexto delega el trabajo a la estrategia inyectada.

```python
carrito = Carrito(PagoTarjeta())   # Paga con tarjeta
carrito = Carrito(PagoPayPal())    # Cambia a PayPal sin modificar Carrito
```

---

### Observer

**¿Cuándo usarlo?**
- Cuando un cambio en un objeto debe notificar automáticamente a otros objetos.
- Cuando no sabes de antemano cuántos objetos necesitan reaccionar al cambio.
- Ejemplos: sistemas de eventos, notificaciones en tiempo real, actualización de UI, suscripciones a datos.

**¿Cómo funciona?**
El objeto observable mantiene una lista de suscriptores. Cuando su estado cambia, recorre la lista y notifica a cada suscriptor. Los suscriptores se registran y desregistran dinámicamente.

```python
tienda.evento_nuevo_producto.suscribir(enviar_email)
tienda.evento_nuevo_producto.suscribir(notificar_app)
tienda.agregar_producto("Laptop")  # Ambos suscriptores son notificados
```

---

### Command

**¿Cuándo usarlo?**
- Cuando quieres parametrizar objetos con operaciones.
- Cuando necesitas implementar operaciones reversibles (deshacer/rehacer).
- Cuando quieres encolar, registrar o programar operaciones.
- Ejemplos: editores de texto, transacciones, sistemas de macros, colas de tareas.

**¿Cómo funciona?**
Encapsula una solicitud como un objeto que contiene toda la información necesaria para ejecutarla. Esto permite almacenar comandos en un historial, deshacerlos, o ejecutarlos en diferido.

```python
historial.ejecutar(ComandoEscribir(editor, "Hola"))
historial.deshacer()  # Revierte el último comando ejecutado
```

---

## Resumen rápido

| Patrón | Categoría | Problema que resuelve |
|--------|-----------|----------------------|
| Singleton | Creacional | Necesito una sola instancia global |
| Factory Method | Creacional | No sé qué tipo de objeto crear hasta tiempo de ejecución |
| Builder | Creacional | El objeto es complejo de construir |
| Adapter | Estructural | Dos interfaces incompatibles deben trabajar juntas |
| Decorator | Estructural | Necesito añadir comportamiento sin modificar la clase |
| Facade | Estructural | El subsistema es demasiado complejo para el cliente |
| Strategy | Comportamiento | Necesito intercambiar algoritmos dinámicamente |
| Observer | Comportamiento | Varios objetos deben reaccionar a un cambio |
| Command | Comportamiento | Necesito encapsular, encolar o deshacer operaciones |

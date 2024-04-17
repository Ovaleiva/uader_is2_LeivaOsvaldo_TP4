class Componente:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + self.nombre)


class Pieza(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)


class Subconjunto(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.componentes = []

    def agregar_componente(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + self.nombre)
        for componente in self.componentes:
            componente.mostrar(nivel + 1)


class ProductoPrincipal(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.subconjuntos = []

    def agregar_subconjunto(self, subconjunto):
        self.subconjuntos.append(subconjunto)

    def mostrar(self, nivel=0):
        print(self.nombre)
        for subconjunto in self.subconjuntos:
            subconjunto.mostrar(nivel + 1)


# Creación de las piezas
piezas_subconjunto = [Pieza(f"Pieza {i}") for i in range(1, 5)]

# Creación de los subconjuntos
subconjunto_1 = Subconjunto("Subconjunto 1")
subconjunto_2 = Subconjunto("Subconjunto 2")
subconjunto_3 = Subconjunto("Subconjunto 3")

# Agregar piezas a los subconjuntos
[subconjunto_1.agregar_componente(pieza) for pieza in piezas_subconjunto]
[subconjunto_2.agregar_componente(pieza) for pieza in piezas_subconjunto]
[subconjunto_3.agregar_componente(pieza) for pieza in piezas_subconjunto]

# Creación del producto principal
producto_principal = ProductoPrincipal("Producto Principal")

# Agregar subconjuntos al producto principal
producto_principal.agregar_subconjunto(subconjunto_1)
producto_principal.agregar_subconjunto(subconjunto_2)
producto_principal.agregar_subconjunto(subconjunto_3)

# Mostrar la configuración
producto_principal.mostrar()

# Agregar un subconjunto opcional
subconjunto_opcional = Subconjunto("Subconjunto Opcional")
[subconjunto_opcional.agregar_componente(Pieza(f"Pieza Extra {i}")) for i in range(1, 5)]

# Agregar el subconjunto opcional al producto principal
producto_principal.agregar_subconjunto(subconjunto_opcional)

# Mostrar la configuración actualizada
print("\nDespués de agregar el subconjunto opcional:")
producto_principal.mostrar()

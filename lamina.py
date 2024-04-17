class Lamina:
    def __init__(self, espesor, ancho):
        self.espesor = espesor
        self.ancho = ancho

    def producir(self, laminador):
        pass

class LaminaAcero(Lamina):
    def __init__(self, espesor, ancho):
        super().__init__(espesor, ancho)

    def producir(self, laminador):
        laminador.producir(self)

class Laminador:
    def __init__(self, longitud_maxima):
        self.longitud_maxima = longitud_maxima

    def producir(self, lamina):
        pass

class Laminador5Metros(Laminador):
    def __init__(self):
        super().__init__(5)

    def producir(self, lamina):
        print(f"Lámina de {lamina.ancho} metros producida en el laminador de 5 metros.")

class Laminador10Metros(Laminador):
    def __init__(self):
        super().__init__(10)

    def producir(self, lamina):
        print(f"Lámina de {lamina.ancho} metros producida en el laminador de 10 metros.")

if __name__ == "__main__":
    lamina_pequeña = LaminaAcero(0.5, 1.5)
    lamina_grande = LaminaAcero(0.5, 5)

    laminador_5m = Laminador5Metros()
    laminador_10m = Laminador10Metros()

    lamina_pequeña.producir(laminador_5m)
    lamina_grande.producir(laminador_10m)

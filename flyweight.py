class DatosJugador:
    def __init__(self, nombre, nacionalidad, posicion):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.posicion = posicion

class Jugador:
    def __init__(self, datos_jugador, nivel_habilidad):
        self.datos_jugador = datos_jugador
        self.nivel_habilidad = nivel_habilidad

class FabricaJugadores:
    _jugadores = {}

    def obtener_jugador(self, nombre, nacionalidad, posicion, nivel_habilidad):
        clave = (nombre, nacionalidad, posicion)
        if clave not in self._jugadores:
            datos_jugador = DatosJugador(nombre, nacionalidad, posicion)
            self._jugadores[clave] = Jugador(datos_jugador, nivel_habilidad)
        return self._jugadores[clave]


def solicitar_nombre_jugador():
    return input("Ingresa el nombre del jugador: ")

fabrica = FabricaJugadores()

nombre_jugador = solicitar_nombre_jugador()

jugador = fabrica.obtener_jugador(nombre_jugador, "Argentina", "Delantero", 95)
jugador1 = fabrica.obtener_jugador("Lionel Messi", "Argentina", "Delantero", 95)
jugador2 = fabrica.obtener_jugador("Enzo Fernández", "Argentina", "Mediocampista", 88)

print(f"Nombre: {jugador.datos_jugador.nombre}")
print(f"Nacionalidad: {jugador.datos_jugador.nacionalidad}")
print(f"Posición: {jugador.datos_jugador.posicion}")
print(f"Nivel de habilidad: {jugador.nivel_habilidad}")

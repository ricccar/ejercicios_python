"""
Segunda parte:
Crear una clase Reproductor que nos permita reproducir música con un filtro
Ademas, el reproductor debería recordar que canciones ha puesto en orden, y deberíamos de poder cambiar de filtro cuando queramos
"""

class Reproductor:
    def __init__(self, canciones: list, filtro):
        self.canciones = canciones
        self.filtro = filtro

    def reproducir(self, cancion:str, filtro = None):
        self.historial.append(cancion)
        self._aplicar_filtro(cancion, filtro)
        return(f"Iniciando {cancion}")

    def cancion_actual(self):
        return self.cancion_actual[-1]

    def cambiar_filtro(self, filtro: None):
        cancion = self._aplicar_filtro(self.cancion_actual(), filtro)
        return ("fContibnuando {cancion}")


    def _aplicar_filtro(cancion, filtro):
        return filtro(cancion) if filtro else cancion

    # Video Sigue en la 1:02
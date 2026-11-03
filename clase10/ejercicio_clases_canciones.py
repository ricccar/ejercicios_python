"""
Segunda parte:
Crear una clase Reproductor que nos permita reproducir música con un filtro
Ademas, el reproductor debería recordar que canciones ha puesto en orden, y deberíamos de poder cambiar de filtro cuando queramos
"""

class Reproductor:
    def __init__(self):
        self.historico = []

    def reproducir(self, cancion:str, filtro = None):
        self.historico.append(cancion)
        cancion = self._aplicar_filtro(cancion, filtro)
        return(f"Iniciando {cancion}")

    def cancion_actual(self):
        return self.historico[-1]

    def cambiar_filtro(self, filtro: None):
        cancion = self._aplicar_filtro(self.cancion_actual(), filtro)
        return (f"Contibnuando {cancion}")

    @staticmethod
    def _aplicar_filtro(cancion, filtro):
        return filtro(cancion) if filtro else cancion

def solo_epico(cancion: str):
    return cancion.upper()

def repetir(cancion: str):
    return ((cancion+" ")*5)

c = "The river"
c2 = "Moonlight"

repr = Reproductor()
print(repr.reproducir(c, solo_epico))
print(repr.historico)
print(repr.reproducir(c2, repetir))
print(repr.historico)
print(repr.cambiar_filtro(solo_epico))
print(repr.historico)


"""
Ejercicio:
Estamos programando para un DJ en una fiesta, el quiere que le hagamos una función para pasarle una canción y aplique un filtro de musica
la idea es que la función funcione así:
pinchar_musica(canción, filtro)
por ejemplo:
pinchar_musica("Smoke on the water", solo_epico)
"""

def solo_epico(cancion: str):
    return cancion.upper()

def vol_max(cancion: str):
    return len(cancion)

def repetir(cancion: str, veces: int):
    return ((cancion+" ")*veces)

def pinchar_musica(cancion: str, filtros: function, *args):
    cancion_filtrada = filtros(cancion, *args)
    return cancion_filtrada


cancion = "The River"
print(pinchar_musica(cancion, solo_epico))
print(pinchar_musica(cancion, vol_max))
print(pinchar_musica(cancion, repetir, 7))

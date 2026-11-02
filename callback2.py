# Callback
def funcion(otra_funcion, argumento):       # Aquí tengo mi callback
    return otra_funcion(argumento)          # callback  (la otra funcion)

def sumar(lista_numeros):       # funcion cualquiera
    return sum(lista_numeros)

resultado = funcion(sumar, [1,2,3,5,6])
print(resultado)


# Callback2
def funcion2(otra_funcion, argumento1, argumento2):       # Aquí tengo mi callback
    return otra_funcion(argumento1, argumento2)          # callback  (la otra funcion)

def sumar(n1, n2):       # funcion cualquiera
    return n1 + n2

resultado2 = funcion2(lambda n1, n2: n1 - n2, 10, 20)
print(resultado2)


# Ejemplo Callback3

class CarritoCompra:
    def __init__(self, usuario, productos = []):
        self.usuario = usuario
        self.productos = productos
        self.ultimo_estado = None

    def añadir_producto(self, producto_nuevo):
        if producto_nuevo not in self.productos:
            self.productos.append(producto_nuevo)

    def eliminar_producto(self, indice):
        self.productos.pop(indice)

    def info_productos(self):
        print(f"Tus productos son : {self.productos}")

    def procesar(self, callback: function):
        self.ultimo_estado = callback(self.productos)


historial = []
contador = 1
def añadir_historial(lista_items):
    global contador
    historial.append(f"{contador} - {lista_items}")
    contador += 1


carrito = CarritoCompra("ricar", [])
carrito.info_productos()
carrito.añadir_producto("Camiseta")
carrito.añadir_producto("Armario")
carrito.añadir_producto("Librería")
carrito.añadir_producto("Pantalón")
carrito.añadir_producto("Cámara de fotos")
#carrito.info_productos()
#carrito.procesar(print)
#carrito.procesar(sorted)
#print(carrito.ultimo_estado)
carrito.procesar(añadir_historial)
carrito.eliminar_producto(2)
carrito.eliminar_producto(0)
carrito.procesar(añadir_historial)
carrito.añadir_producto("Ajedrez")
carrito.añadir_producto("Lámpara")
carrito.procesar(añadir_historial)
carrito.info_productos()
for log in historial:
    print(log)
print(historial)


"""
Podría ser con argumentos:
    def procesar(self, callback: function, *args):
        self.ultimo_estado = callback(self.productos, *args)
"""
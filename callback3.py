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

    def procesar(self, callback: function, *args):
        self.ultimo_estado = callback(self.productos, *args)
        return self.ultimo_estado


historial = []
contador = 1
def añadir_historial(lista_items):
    global contador
    historial.append(f"{contador} - {lista_items}")
    contador += 1

def filtrar_por_letra(lista_items, letra):
    lista_final = []
    for item in lista_items:
        if item.startswith(letra):
            lista_final.append(item)
    return lista_final


carrito = CarritoCompra("ricar", [])
carrito.añadir_producto("Camiseta")
carrito.añadir_producto("Armario")
carrito.añadir_producto("Librería")
carrito.añadir_producto("Pantalón")
carrito.añadir_producto("Cámara de fotos")
carrito.añadir_producto("Abrigo")
carrito.añadir_producto("Acuarela")
carrito.añadir_producto("Blusa")
resultado = carrito.procesar(filtrar_por_letra, "A")
print(resultado)
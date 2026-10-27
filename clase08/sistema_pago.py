class SistemaPagos:
    def __init__(self, _id: int, entidad: str, destinatario: str):
        self.id = _id
        self.entidad = entidad
        self.destinatario = destinatario

    def pagar(self):
        print(f"Se ha pagado correctamente a {self.destinatario}")

# Dinaero y forma de pago

class PagpPaypal(SistemaPagos):
    def procesar_pago(self, cantidad: float):
        self.forma_pago = "paypal"
        self.ultima_cantidad_pagada = cantidad
        print(f"Se ha pagado {cantidad} a {self.destinatario}")

class PagoCredito(SistemaPagos):
    def procesar_pago(self, cantidad: float):
        self.forma_pago = "credito"
        self.ultima_cantidad_pagada = cantidad
        print(f"Se ha pagado {cantidad} a {self.destinatario}")


sp = PagoCredito(1, "Banco Santander", "20202020H")
sp.procesar_pago(1000)
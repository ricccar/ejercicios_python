class Cliente:
    def __init__(self, _id: int, nombre_completo: list[str], edad: int,
                 cantidad_dinero: float, plataforma_de_pago: str = "al contado",
<<<<<<< HEAD
                 # [("pan", 1.20), ...]
                 carrito_compra: list[tuple[str, float]] = []):
=======
                 carrito_compra: list[tuple[str, float]] = []):  # [("pan", 1.20), ...]
>>>>>>> 167aba0f6d3ded518957dc26474cfb86613e5a4d
        self._id = _id
        self.nombre = nombre_completo[0]
        self.apellido = nombre_completo[1]
        self.edad = edad
        self.cantidad_dinero = cantidad_dinero
        self.plataforma = plataforma_de_pago
        self.carrito = carrito_compra  # ("pan", 1.20)

    def hacer_compra(self, dinero_a_pagar: float):
        self.cantidad_dinero -= dinero_a_pagar
<<<<<<< HEAD
        print(
            f"Se ha pagado mediante {self.plataforma} {dinero_a_pagar}€ y te quedan {self.cantidad_dinero}€")
=======
        print(f"Se ha pagado mediante {self.plataforma} {dinero_a_pagar}€ y te quedan {self.cantidad_dinero}€")
>>>>>>> 167aba0f6d3ded518957dc26474cfb86613e5a4d

    def validar_compra(self):
        total_a_pagar = 0
        for item in self.carrito:
            total_a_pagar += item[1]  # lo que vale
        if self.cantidad_dinero < total_a_pagar:
            print("No se puede pagar!")
            return False
        else:
            self.hacer_compra(total_a_pagar)
        return True

    def validar_menor_edad(self):
        if self.edad < 18:
            print("Los menores de edad no pueden pagar")
            return False
        else:
            return True

    def añadir_item_al_carrito(self, item: tuple[str, float]):
        self.carrito.append(item)

    def eliminar_item_del_carrito(self, indice_item: int):
        item_eliminado = self.carrito.pop(indice_item)
        print(f"Se ha eliminado {item_eliminado[0]}")

    def mostrar_carrito(self):
        print(self.carrito)

    def procesar(self):
        print(f"Estoy haciendo el pago en {self.plataforma}")
        if not self.validar_menor_edad():
            return False
        if self.validar_compra():
            print("Todo correcto")
            return True
        else:
            return False

<<<<<<< HEAD

joa = Cliente(1, "Joaquin Hernandez", 10, 1700.0, "paypal")
=======
joa = Cliente(1, "Joaquin Hernandez", 19, 1900.0, "paypal")
>>>>>>> 167aba0f6d3ded518957dc26474cfb86613e5a4d
joa.añadir_item_al_carrito(("ordenador", 900))
joa.añadir_item_al_carrito(("compra_del_mes", 650.23))
joa.añadir_item_al_carrito(("sumistros", 200.10))
joa.mostrar_carrito()
joa.procesar()
<<<<<<< HEAD
print(joa.cantidad_dinero)
=======
print(joa.cantidad_dinero)
>>>>>>> 167aba0f6d3ded518957dc26474cfb86613e5a4d

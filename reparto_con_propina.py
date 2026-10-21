def repartir_cuenta(pagos: list[tuple[str, float]], propina: float = 0) -> float:
    """
    Calcula la cantidad que debe pagar cada persona para cubrir
    el total de la cuenta del restaurante, incluyendo una propina opcional.

    :param pagos: Una lista de tuplas donde cada tupla contiene el nombre de la
                  persona (str) y la cantidad que pagó o consumió (float).
    :param propina: Cantidad fija de dinero que se sumará al total de la cuenta
                    antes de dividirlo. Por defecto es 0.
    :return: El coste total por persona (la media con la propins incluida).
    """

    total_consumido = 0
    for _, elemento in pagos:
        total_consumido += elemento
    total_con_propina = total_consumido + propina
    numero_personas = len(pagos)
    return total_con_propina / numero_personas


pagos_amigos = [
    ("Ana", 18.50),
    ("Luis", 24.00),
    ("Marta", 15.50),
    ("Pedro", 22.00)
]


reparto_sin_propina = repartir_cuenta(pagos_amigos)
print(f"Cada uno debe pagar (sin propina): {reparto_sin_propina:.2f}€")


reparto_con_propina = repartir_cuenta(pagos_amigos, propina=4)
print(f"Cada uno debe pagar (con propina): {reparto_con_propina:.2f}€")

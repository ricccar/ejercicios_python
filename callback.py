import math

# --- 1. FUNCIÓN PRINCIPAL CON CALLBACK ---


def validar(numero, callback=None):
    """
    Realiza validaciones matemáticas básicas en un número y opcionalmente
    ejecuta una lógica adicional mediante un callback.
    """
    # Determinamos si es entero o flotante
    es_entero = isinstance(numero, int) or (
        isinstance(numero, float) and numero.is_integer())

    # Normalizamos el valor para las pruebas de par/impar/primo si actúa como entero
    valor_analizar = int(numero) if es_entero else numero

    # Validaciones básicas
    resultado_base = {
        "numero": numero,
        "tipo": "entero" if es_entero else "flotante",
        "par": valor_analizar % 2 == 0 if es_entero else None,
        "impar": valor_analizar % 2 != 0 if es_entero else None,
        "primo": es_primo(valor_analizar) if es_entero else False
    }

    # Si se proporciona un callback, se ejecuta pasando el resultado base
    if callback:
        return callback(resultado_base)

    return resultado_base


# --- FUNCIÓN AUXILIAR ---
def es_primo(n):
    """Determina si un número entero es primo."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# --- 2. CALLBACKS CON LAS TRES LÓGICAS ADICIONALES ---

def callback_edad(datos_num):
    """Lógica para validar si es mayor o menor de edad."""
    num = datos_num["numero"]
    # Asumimos la mayoría de edad a los 18 años
    datos_num["contexto"] = "Edad"
    datos_num["estado"] = "Mayor de edad" if num >= 18 else "Menor de edad"
    return datos_num


def callback_neumatico(datos_num):
    """Lógica para validar la presión de un neumático (Rango: 180 a 460)."""
    num = datos_num["numero"]
    datos_num["contexto"] = "Presión de Neumático"
    if 180 <= num <= 460:
        datos_num["estado"] = "Presión adecuada"
    else:
        datos_num["estado"] = "Presión fuera de rango (Inadecuada)"
    return datos_num


def callback_intentos(datos_num):
    """Lógica para bloquear al usuario si supera los 3 intentos."""
    num = datos_num["numero"]
    datos_num["contexto"] = "Intentos de Usuario"
    datos_num["estado"] = "Usuario BLOQUEADO temporalmente" if num > 3 else "Acceso permitido"
    return datos_num


# --- 3. PRUEBAS DE EJECUCIÓN ---

print("--- Prueba 1: Validación básica (Sin callback) ---")
print(validar(7))
print(validar(4.5))

print("\n--- Prueba 2: Lógica de Edad ---")
resultado_edad = validar(17, callback=callback_edad)
print(
    f"Número {resultado_edad['numero']} ({resultado_edad['tipo']}): {resultado_edad['estado']}")

print("\n--- Prueba 3: Lógica de Neumáticos ---")
resultado_presion = validar(220, callback=callback_neumatico)
print(f"Presión {resultado_presion['numero']}: {resultado_presion['estado']}")

print("\n--- Prueba 4: Lógica de Intentos ---")
resultado_intentos = validar(4, callback=callback_intentos)
print(
    f"Intentos {resultado_intentos['numero']}: {resultado_intentos['estado']}")

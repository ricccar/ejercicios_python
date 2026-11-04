# Aquí establecemos el menú de la calculadora
import operaciones


def pedir_operadores():
    n1 = float(input("introduce el primer valor: "))
    n2 = float(input("introduce el segundo valor: "))
    return n1, n2

def menu():
    while True:
        print("\n=================================")
        print("  CALCULADORA  ")
        print("=================================")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Raiz")
        print("7. Salir")

        opcion = input("Selecciona una opción (1-7): ")

        if opcion == "1":
            n1, n2 = pedir_operadores()
            print(f"La suma de {n1} + {n2} = {operaciones.sumar(n1,n2)}")
        elif opcion == "2":
            n1, n2 = pedir_operadores()
            print(f"La resta de {n1} - {n2} = {operaciones.restar(n1,n2)}")
        elif opcion == "3":
            n1, n2 = pedir_operadores()
            print(f"La multiplicación de {n1} * {n2} = {operaciones.multiplicar(n1,n2)}")
        elif opcion == "4":
            n1, n2 = pedir_operadores()
            print(f"La división de {n1} * {n2} = {operaciones.dividir(n1,n2)}")
        elif opcion == "5":
            n1, n2 = pedir_operadores()
            print(f"{n1} elevado a la {n2} = {operaciones.elevar(n1,n2)}")
        elif opcion == "6":
            n1, n2 = pedir_operadores()
            print(f"La raiz {n2}ª de {n1} = {operaciones.raiz(n1,n2)}")
        elif opcion == "7":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()

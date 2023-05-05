"""
Calculadora
------------------------------------------------------------------------------------------
"""


def suma(num1, num2):
    if isinstance(num1, float) and isinstance(num2, float):
        return num1 + num2
    else:
        return "No se puede sumar eso"


def resta(num1, num2):
    if isinstance(num1, float) and isinstance(num2, float):
        return num1 - num2
    else:
        return "No se puede restar eso"


def multiplicacion(num1, num2):
    if isinstance(num1, float) and isinstance(num2, float):
        return num1 * num2
    else:
        return "No se puede multiplicar eso"


def division(num1, num2):
    if isinstance(num1, float) and isinstance(num2, float):
        if num2 != 0:
            return num1 / num2
        else:
            return "Division entre 0"
    else:
        return "No se puede dividir eso"


def calculadora():
    while True:
        print("Que quieres hacer?")
        print("Sumar [+]")
        print("Resta [-]")
        print("Multiplicar [*]")
        print("Dividir [/]")
        print("Salir [Lo que sea]")
        operacion = input()
        if operacion not in ("+", "-", "*", "/"):
            break
        while True:
            valor1 = input("Primer valor: ")
            try:
                num1 = float(valor1)
                break
            except ValueError:
                print("No es un numero")

        while True:
            valor2 = input("Segundo valor: ")
            try:
                num2 = float(valor2)
                break
            except ValueError:
                print("No es un numero")

        if operacion == "+":
            print(suma(num1, num2))
        elif operacion == "-":
            print(resta(num1, num2))
        elif operacion == "*":
            print(multiplicacion(num1, num2))
        elif operacion == "/":
            print(division(num1, num2))
        else:
            break
        print("")
    print("Hasta otra")


calculadora()
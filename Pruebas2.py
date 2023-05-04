import random as rd


class MyEx(Exception):
    def __init__(self, message):
        self.message = message
        super.__init__(message)


def comprobadorentero(a):
    if type(a) == int:
        raise MyEx("No es un numero entero")


def cantdados():
    cant = input("Cuantos dados quieres lanzar? ")
    try:
        num = int(cant)
        if num != 0:
            print("Perfecto!")
        return num
    except ValueError:
        print("No es un numero entero")
        return 0


def tirardados():
    min_val = 1
    max_val = 6
    seguir = "y"
    while seguir.lower() == "y":
        valores = []
        tot = 0
        while True:
            cant = cantdados()
            if cant != 0:
                break
        print("Tirando dados...")
        for x in range(cant):
            valor = rd.randint(min_val, max_val)
            valores.append(valor)
            print("Dado: ", valor)
            tot += valor
        print("Total: ", tot)
        seguir = input("Continuar? (y) ")
    print("Hasta otra")


tirardados()

"""
Tic Tac Toe
-------------------------------------------------------------
"""


import random as rd


class TresRaya:
    def __init__(self):
        self.board = []
        if rd.randint(0, 1) == 1:
            self.jugador = "X"
        else:
            self.jugador = "O"

    def crear_tab(self):
        for i in range(3):
            columna = []
            for j in range(3):
                columna.append('-')
            self.board.append(columna)

    def ver(self):
        for x in self.board:
            print(x)

    def poner_ficha(self, fila, columna, jugador):
        if self.board[fila-1][columna-1] == "-":
            self.board[fila-1][columna-1] = jugador
            return True
        else:
            return False

    def ganador(self, jugador):
        valores = set()
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                valores.add(self.board[x][y])
        if valores == {jugador}:
            return True
        else:
            valores.clear()
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                valores.add(self.board[y][x])
        if valores == {jugador}:
            return True
        else:
            valores.clear()
        for x in range(len(self.board)):
            valores.add(self.board[x][x])
        if valores == {jugador}:
            return True
        else:
            valores.clear()
        valores.add(self.board[0][2])
        valores.add(self.board[2][2])
        valores.add(self.board[2][0])
        if valores == {jugador}:
            return True
        else:
            return False

    def cambiar(self):
        if self.jugador == "X":
            self.jugador = "O"
        else:
            self.jugador = "X"

    def juego(self):
        self.crear_tab()
        while True:
            print(f"Jugador {self.jugador}")
            self.ver()
            fila = int(input("Fila: "))
            columna = int(input("Columna: "))
            poder = self.poner_ficha(fila, columna, self.jugador)
            while not poder:
                print("no puedes")
                self.ver()
                fila = int(input("Fila: "))
                columna = int(input("Columna: "))
                poder = self.poner_ficha(fila, columna, self.jugador)

            if self.ganador(self.jugador):
                print(f"felicidades ganó {self.jugador}")
                break
            self.cambiar()


y = TresRaya()
y.juego()


"""
El Ahorcado
---------------------------------------------------
"""

import random as rd
import time


def escoger_p():
    lista_palabras = ["elefante", "ordenador", "pantalla", "cable", "europa", "palabra", "mochila"]
    return rd.choice(lista_palabras)


def juego(escogida):
    letras = []
    palabra = list(escogida)
    mostrar = "_" * len(escogida)
    contador = 0
    limite = 5
    while contador < limite:
        guess = input(f"Palabra {mostrar} \nDi una letra: ").strip()
        while len(guess) != 1:
            print("Solo una letra!")
            guess = input(f"Palabra {mostrar} \nDi una letra: ").strip()
        if guess in letras:
            print("Ya has dicho esta letra")
            continue
        if guess in palabra:
            letras.append(guess)
            print(guess, " esta en la palabra")
            palabra.remove(guess)
            indice = -1
            while True:
                indice = escogida.find(guess, indice + 1)
                if indice == -1:
                    break
                mostrar = mostrar[:indice] + guess + mostrar[indice + 1:]
        else:
            letras.append(guess)
            print(guess, " no esta en la palabra")
            contador += 1
            if contador == 1:
                time.sleep(1)
                print('   _____ \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '__|__\n')
                print(f'Lastima: te quedan {limite - contador} oportunidades\n')

            elif contador == 2:
                time.sleep(1)
                print('   _____ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '__|__\n')
                print(f'Lastima: te quedan {limite - contador} oportunidades\n')

            elif contador == 3:
                time.sleep(1)
                print('   _____ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '__|__\n')
                print(f'Lastima: te quedan {limite - contador} oportunidades\n')

            elif contador == 4:
                time.sleep(1)
                print('   _____ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     O \n'
                      '  |      \n'
                      '  |      \n'
                      '__|__\n')
                print(f'Lastima: te quedan {limite - contador} oportunidades\n')

            elif contador == limite:
                time.sleep(1)
                print('   _____ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     O \n'
                      '  |    /|\ \n'
                      '  |    / \ \n'
                      '__|__\n')
                print(f'Lastima: te quedan {limite - contador} oportunidades\n')
                print(f'La palabra era: {escogida}')

        if mostrar == escogida:
            print(f'Felicidades! La palabra era \'{escogida}\' !')
            break


palabra = escoger_p()
juego(palabra)

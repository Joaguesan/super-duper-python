"""
Generador de contraseñas
"""
import secrets
import string
import csv
import os


def generador(nombre, longitud=8):
    letrasmay = string.ascii_uppercase
    letrasmin = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation
    simbolos = simbolos.replace("\'", "")
    simbolos = simbolos.replace("\"", "")
    simbolos = simbolos.replace("`", "")
    simbolos = simbolos.replace(",", "")
    opciones = letrasmay + numeros + simbolos + letrasmin
    contr = ""
    fuerte = False
    while not fuerte:
        for x in range(longitud):
            contr += "".join(secrets.choice(opciones))
        simbs = sum(char in simbolos for char in contr) >= 2
        nums = sum(char in numeros for char in contr) >= 2
        mays = any(char in letrasmay for char in contr)
        mins = any(char in letrasmin for char in contr)
        if simbs and nums and mays and mins:
            fuerte = True
        else:
            contr = ""
    if os.path.exists("./contr.csv"):
        with open('./contr.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([nombre, contr])
    else:
        with open('./contr.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['Sitio Web', 'contraseña'])
            writer.writerow([nombre, contr])


print(generador("Facebook", 8))

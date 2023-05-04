"""
Revision de contraseñas
-------------------------------------------------------------
"""


import getpass


def revisor():
    pwd = getpass.getpass('Enter the password: ')
    nums = mays = mins = simb = seguridad = 0
    for x in list(pwd):
        if x.isupper():
            mays += 1
        elif x.islower():
            mins += 1
        elif x.isdigit():
            nums += 1
        elif not x.isalpha() and not x.isspace():
            simb += 1
    if mays >= 1:
        seguridad += 1
    if mins >= 1:
        seguridad += 1
    if nums >= 1:
        seguridad += 1
    if simb >= 1:
        seguridad += 1
    print(f"Tienes {mays} mayusculas, {mins} minusculas, {nums} numeros y {simb} simbolos")
    if seguridad == 1:
        return "muy debil"
    elif seguridad == 2:
        return "debil"
    elif seguridad == 3:
        return "media"
    elif seguridad == 4:
        return "fuerte"
    elif seguridad == 5:
        return "muy fuerte"


print("Seguridad", revisor())

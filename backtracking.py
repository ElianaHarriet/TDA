"""
Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros
para iluminarlos a todos. Implementar un algoritmo que dé la cantidad mínima de faros
que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro
ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las
directamente adyacentes a estas (es decir, un “radio de 2 celdas”). 
"""
from copy import deepcopy

def iluminado(matriz, coords):
    x, y = coords
    min_x, max_x = max(x - 2, 0), min(x + 2, len(matriz) - 1)
    min_y, max_y = max(y - 2, 0), min(y + 2, len(matriz[0]) - 1)
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if matriz[i][j] == "FARO":
                return True
    return False

def faros_backtracking(matriz, submarinos, cantidad):
    if len(submarinos) == 0:
        return matriz, cantidad

    x, y = submarinos[0]

    if iluminado(matriz, (x, y)):
        return faros_backtracking(matriz, submarinos[1:], cantidad)

    min_x, max_x = max(x - 2, 0), min(x + 2, len(matriz) - 1)
    min_y, max_y = max(y - 2, 0), min(y + 2, len(matriz[0]) - 1)

    opciones = []

    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if matriz[i][j] == "SUBMARINO":
                continue
            matriz[i][j] = "FARO"
            opciones.append(faros_backtracking(deepcopy(matriz), submarinos[1:], cantidad + 1))
            matriz[i][j] = "AGUA"

    return min(opciones, key=lambda x: x[1])


def faros(matriz):
    submarinos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == "SUBMARINO":
                submarinos.append((i, j))
    return faros_backtracking(matriz, submarinos, 0)[1]

matriz = [
    ["AGUA",    "AGUA",     "AGUA",     "AGUA",     "AGUA"],
    ["AGUA",    "AGUA",     "AGUA",     "AGUA",     "AGUA"],
    ["AGUA",    "AGUA",     "AGUA",     "AGUA",     "AGUA"],
    ["AGUA",    "AGUA",     "AGUA",     "AGUA",     "AGUA"],
    ["AGUA",    "AGUA",     "AGUA",     "AGUA",     "AGUA"],
]
print(faros(matriz))

matriz = [
    ["AGUA",    "SUBMARINO",    "AGUA",     "AGUA",         "AGUA"],
    ["AGUA",    "AGUA",         "AGUA",     "AGUA",         "AGUA"],
    ["AGUA",    "AGUA",         "AGUA",     "AGUA",         "AGUA"],
    ["AGUA",    "AGUA",         "AGUA",     "SUBMARINO",    "AGUA"],
    ["AGUA",    "AGUA",         "AGUA",     "AGUA",         "AGUA"],
]
print(faros(matriz))

matriz = [
    ["AGUA",    "SUBMARINO",    "AGUA",     "AGUA",         "AGUA"],
    ["AGUA",    "AGUA",         "AGUA",     "AGUA",         "AGUA"],
    ["AGUA",    "AGUA",         "AGUA",     "AGUA",         "AGUA"],
    ["AGUA",    "AGUA",         "AGUA",     "SUBMARINO",    "AGUA"],
    ["AGUA",    "SUBMARINO",    "AGUA",     "AGUA",         "AGUA"],
]
print(faros(matriz))

matriz = [
    ["SUBMARINO",    "AGUA",         "AGUA",         "AGUA",         "SUBMARINO",   "AGUA",         "AGUA",         "AGUA",     ],
    ["AGUA",         "AGUA",         "AGUA",         "AGUA",         "AGUA",        "AGUA",         "AGUA",         "AGUA",     ],
    ["AGUA",         "AGUA",         "AGUA",         "AGUA",         "AGUA",        "AGUA",         "AGUA",         "AGUA",     ],
    ["AGUA",         "AGUA",         "AGUA",         "AGUA",         "AGUA",        "AGUA",         "AGUA",         "SUBMARINO",],
    ["AGUA",         "AGUA",         "AGUA",         "AGUA",         "AGUA",        "AGUA",         "AGUA",         "AGUA",     ],
    ["AGUA",         "SUBMARINO",    "AGUA",         "AGUA",         "AGUA",        "AGUA",         "AGUA",         "AGUA",     ],
    ["AGUA",         "AGUA",         "AGUA",         "AGUA",         "AGUA",        "AGUA",         "SUBMARINO",    "AGUA",     ],
]
print(faros(matriz))
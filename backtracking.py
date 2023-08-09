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

"""
2.
Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah
decidió que en una misma parada de colectivo nunca pararán dos colectivos que usen el mismo
color. El problema es que ya saben que eso está sucediendo hoy en día, así que van a repintar
todas las líneas de colectivos. Por problemas presupuestarios, sólo pueden pintar los colectivos
de k colores diferentes (por ejemplo, k = 4, pero podría se otro valor). Como no quieren parecer
un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber
si es posible cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal forma
que no hayan dos de mismo color coincidiendo en la misma parada).
Considerando que se tiene la información de todas las paradas de colectivo y qué líneas paran allí,
modelar el problema utilizando grafos e implementar un algoritmo que determine si es posible resolver
el problema.
Indicar la complejidad del algoritmo implementado. 
"""

def hay_conflictos(grafo, coloreado, v):
    for w in grafo.adyacentes(v):
        if coloreado[w] == coloreado[v]:
            return True
    return False


def k_coloreo(grafo, k, vertices, coloreados):
    if len(vertices) == 0:
        return True
    
    v = vertices.pop(0)

    for color in range(k):
        coloreados[v] = color
        if not hay_conflictos(grafo, coloreados, v):
            if k_coloreo(grafo, k, vertices, coloreados):
                return True
        coloreados[v] = None

    vertices.insert(0, v)
    return False
    
def colectivos(grafo, k):
    vertices = grafo.obtener_vertices()
    coloreados = {v: None for v in vertices}
    return k_coloreo(grafo, k, vertices, coloreados)

# O(k^n) -> por cada vertice, tengo k opciones de coloreo
    

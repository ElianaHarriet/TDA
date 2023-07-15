"""
.. 1 ..
Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El
listado (ordenado por nombre del pueblo) contiene el número de kilómetro donde
está ubicada cada una. Se desea ubicar la menor cantidad de patrullas policiales (en
las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a menos de
50 km.

Ejemplo:
    Ciudad      Bifurcación
    Castelli    185
    Gral Guido  249
    Lezama      156
    Maipú       270
    Sevigne     194

    Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. Pero
    no Gral Guido y Maipú. Necesitaría en ese caso, poner otro. Agrego otro patrullero en Gral
    Guido. Con eso tengo 2 móviles policiales en bifurcaciones que cubren todas los accesos a
    todas las ciudades con distancia menor a 50km.

Proponer un algoritmo que lo resuelva. Justificar que la solución es óptima
"""

lista = [("Castelli", 185), ("Gral Guido", 249), ("Lezama", 156), ("Maipú", 270), ("Sevigne", 194)]

def patrullas(lista):
    lista.sort(key=lambda x: x[1])

    patrullas_lista = []
    for i in range(len(lista)):
        if len(patrullas_lista) == 0:
            if lista[i][1] - lista[0][1] >= 50:
                patrullas_lista.append(lista[i - 1])
            continue

        if lista[i][1] - patrullas_lista[-1][1] >= 50:
            patrullas_lista.append(lista[i])
    return patrullas_lista

# print("Patrullas: ", patrullas(lista))

"""
... 4 ...
Los grupos sanguíneos de las personas son cuatro: A, B, O y AB. Los pacientes se clasifican según
su grupo sanguíneo. Un paciente O sólo puede recibir sangre O, un paciente A sólo puede recibir
sangre A u O, un paciente B sólo puede recibir sangre B u O, un paciente AB puede recibir cualquier
grupo sanguíneo. Diseñar una estrategia greedy para resolver el siguiente problema: Sean Sa, Sb, So,
Sab la sangre disponible de cada uno de los grupos y Pa, Pb, Po, Pab los pacientes de cada grupo que
concurren al hospital para recibir una unidad de transfusión. Informar cómo se puede satisfacer la
demanda de sangre de los pacientes (o si no se puede satisfacer). Justificar. 
"""

"""
Matriz de adyacencias para las donaciones
    A   B   O   AB -> donar
A  ✅  ❌  ✅  ❌
B  ❌  ✅  ✅  ❌
O  ❌  ❌  ✅  ❌
AB ✅  ✅  ✅  ✅
-> recibir

1. Reciben los O
2. Reciben los A (sólo de los A)
3. Reciben los B (sólo de los B)
4. Si no recibieron todos los A, los restantes A reciben de los O
5. Si no recibieron todos los B, los restantes B reciben de los O
6. Reciben los AB
"""

"""
.. 6 ..
Una fotocopiadora cada mañana recibe un conjunto de pedidos de clientes. El pedido del cliente i demora
ti en ejecutarse. Para una planificación dada (es decir un cierto orden de las tareas) Ci es la hora en
la cual el pedido i termina de ejecutarse (por ejemplo, si el pedido j es el primero que se ejecuta,
Cj = tj; si el pedido j se ejecuta a continuación del pedido i, Cj=Ci+tj). Cada cliente tiene un peso wi
que representa su importancia. Se supone que la felicidad de un cliente depende de cuán rápido le
entregan el trabajo, por lo que la empresa decide minimizar el tiempo de demora ponderado = Suma (wi * Ci).
Diseñar un algoritmo greedy eficiente para resolver este problema. Calcular su eficiencia temporal y
espacial. Justificar la optimalidad de la solución. 
"""

lista = [(5, 10), (4, 3), (6, 6), (2, 10), (10, 1)] # (ti, wi)

def fotocopiadora(lista):
    # Ordeno por wi/ti, pero no inplace
    return sorted(lista, key=lambda x: x[1] / x[0], reverse=True)

def calcular_suma(lista):
    suma = 0
    ci = 0
    for i in range(len(lista)):
        ci += lista[i][0]
        suma += lista[i][1] * ci
    return suma

print("Orden: ", fotocopiadora(lista))
print("Suma: ", calcular_suma(fotocopiadora(lista)))

def todas_las_permutaciones(lista):
    if len(lista) == 1:
        return [lista]
    else:
        permutaciones = []
        for i in range(len(lista)):
            permutaciones += [[lista[i]] + p for p in todas_las_permutaciones(lista[:i] + lista[i + 1:])]
        return permutaciones

# print("Todas las permutaciones: ", todas_las_permutaciones(lista))

def suma_minima(lista):
    permutaciones = todas_las_permutaciones(lista)
    suma_minima = calcular_suma(permutaciones[0])
    for i in range(1, len(permutaciones)):
        suma = calcular_suma(permutaciones[i])
        if suma < suma_minima:
            suma_minima = suma
    return suma_minima

# print("Suma minima: ", suma_minima(lista))


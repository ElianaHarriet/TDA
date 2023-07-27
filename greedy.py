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

# print("Orden: ", fotocopiadora(lista))
# print("Suma: ", calcular_suma(fotocopiadora(lista)))

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

"""
... Modelo 01 de final ...
Una empresa de telecomunicaciones ganó una licitación para construir un conjunto de “r”
líneas de comunicación bidireccional para “n” ciudades (r<n). Algunas de estas ciudades
ya se encuentran previame nte unidas. Cada línea de comunicación “l” une dos ciudades y
de generarla le permite obtener una ganancia mensual Gl. Puede elegir construir
cualquier línea a menos que una nueva línea conecte 2 ciudades previamente conectadas.
Se considera que 2 ciudades están unidas si existe un camino de líneas que permitan
llegar de una a otra. Nos solicitan nuestro asesoramiento para determinar qué líneas
construir maximizando la ganancia obtenida.

Presentar una solución greedy al problema. Explicar la optimalidad del mismo. Analizar
complejidad temporal y espacial ¿Cuál es el valor máximo que puede tomar r? 
"""
from heapq import heappush, heappop
from grafo import *

# Un árbol de tendido máximo cumple con la consigna
# Prim es un algoritmo que encuentra un árbol de tendido mínimo y es greedy ya que en
# cada paso elige la arista de menor peso sin tener en cuenta futuras aristas
# Se buscará el árbol de tendido máximo, por lo que se pasará el peso negativo de cada
# arista

def max_ganancia(grafo_ciudades):                                              
    arbol = Grafo()
    for v in grafo_ciudades.obtener_vertices():                                
        arbol.agregar_vertice(v)                                                
    
    heap = []
    visitados = set()
    v = grafo_ciudades.vertice_aleatorio()                                     
    visitados.add(v)
    for w in grafo_ciudades.adyacentes(v):                                     
        heappush(heap, (-grafo_ciudades.peso_arista(v, w), v, w))               

    while len(heap) > 0:                                                        
        peso, v, w = heappop(heap)
        if w not in visitados:
            visitados.add(w)
            arbol.agregar_arista(v, w, -peso)
            for x in grafo_ciudades.adyacentes(w):
                heappush(heap, (-grafo_ciudades.peso_arista(w, x), w, x))
    return arbol

"""
(Complejidades asumiendo un grafo implementado como diccionario de diccionarios)

Complejidad temporal:
- Agregar las ciudades al árbol -> O(n)
- Tomar un vértice aleatorio y poner sus adyacentes en el heap -> O(n log n) (como mucho tendrá n adyacentes)
- while -> O(r log n) (como mucho se recorrerán todas las aristas y habrá un múltiplo de n ciudades en el heap)

Total: O(n + nlogn + rlogn) -> n << nlogn << rlogn -> O(rlogn)

Complejidad espacial -> O(r + n) ya que se almacenan r aristas y n vértices

El valor máximo que puede tomar r es n^2, ya que es la cantidad de aristas que puede tener un grafo completo (asume
que no hay aristas repetidas y que puede haber caminos de una ciudad a sí misma)

El algoritmo es óptimo ya que devuelve un árbol de tendido máximo, que es el que maximiza la ganancia
al interconectar todas las ciudades con la menor cantidad de aristas posibles
Es seguro que devolverá el árbol de tendido máximo ya que las aristas elegidas son limitadas, y para toda y cada una
de ellas elegirá siempre la de mayor peso
"""

"""
... Modelo 03 de final ...
Un centro de distribución de repuestos ferroviarios se encuentra en un punto de la red
de este transporte. Es la encargada de distribuir a demanda los materiales y recursos
para las reparaciones que solicitan las diferentes estaciones. Como la red es antigua
y está mal mantenida la cantidad de kilos que se puede transferir sobre cada trayecto
es variable. Esto para ellos es un problema porque quieren enviar la mayor cantidad
posible de material por viaje. Tanto es así que no les importa realizar un camino más
largo siempre que eso implique transportar más materiales.

Se pueden armar diferentes caminos que unan el centro de distribución con cada estación.
Estos estarán conformados por una secuencia de trayectos, cada uno con su propia
limitación de kilos que soporta. Llamamos cuello de botella al valor mínimo entre ellos.

Construir un algoritmo greedy que permita calcular el camino con el máximo cuello de
botella entre el punto de partida y el resto de los puntos. ¿Qué complejidad tiene?
Demuestre que es óptima su solución. 
"""

# Máximo mst??? -> resuelto más arriba

"""
... Modelo 04 de final ...
El proceso de aprobación de trámites de la “central burocrática” está dividido en 2 partes.
La primera parte consiste en una entrevista personalizada cuya duración se puede conocer
según el tipo de trámite. La segunda parte es la revisión de la documentación cuya duración
se calcula previamente mediante una fórmula matemática en función de la persona solicitante.
Cada día se citan “n” personas. Cada una para realizar un trámite. Por cada persona se cuenta,
entonces, con su tiempo de la etapa 1 y su tiempo de la etapa 2. La etapa 1 únicamente la
realiza 1 empleado. Para la etapa 2, hay una cantidad ilimitada de personal para realizarla.
Nuestra tarea es determinar el orden de atención para cada una de las “n”. El objetivo es
minimizar el tiempo total de espera.
Presentar una solución greedy que resuelva el problema. Explicar la optimalidad del mismo. 
"""

personas = {"A": [10, 5], "B": [5, 10], "C": [15, 15], "D": [20, 20], "E": [25, 25]} # (etapa 1, etapa 2)

def orden(personas):
    lista = list(personas.keys())
    lista.sort(key=lambda x: personas[x][0])
    return lista

def orden2(personas):
    lista = list(personas.keys())
    lista.sort(key=lambda x: personas[x][1], reverse=True)
    return lista

# def espera(personas, lista=orden(personas)):
#     esperas = {}
#     comienzo_etapa_1 = 0
#     for persona in lista:
#         if comienzo_etapa_1 < personas[persona][1]:
#             esperas[persona] = comienzo_etapa_1
#         else:
#             esperas[persona] = comienzo_etapa_1 - personas[persona][1]
#         comienzo_etapa_1 += personas[persona][0]
#     return esperas

def sale_ultimo(personas, lista=orden(personas)):
    esperas = {}
    comienzo_etapa_1 = 0
    for persona in lista:
        esperas[persona] = comienzo_etapa_1
        comienzo_etapa_1 += personas[persona][0]
    for persona in lista:
        esperas[persona] += personas[persona][0] + personas[persona][1]
    ultimo = max(esperas, key=lambda x: esperas[x])
    return esperas[ultimo]


# Sí, el algoritmo greedy es más corto que el de calcular los tiempos

# print("Orden: ", orden(personas))
# print("Esperas: ", espera2(personas))
# print("Espera promedio: ", sum(espera2(personas).values()) / len(espera2(personas)))
# print("Espera máxima: ", max(espera2(personas).values()))
# print("Espera total: ", sum(espera2(personas).values()))
# print("--------------------")
# print("Orden 2: ", orden2(personas))
# print("Esperas 2: ", espera2(personas, orden2(personas)))
# print("Espera promedio 2: ", sum(espera2(personas, orden2(personas)).values()) / len(espera2(personas, orden2(personas))))
# print("Espera máxima 2: ", max(espera2(personas, orden2(personas)).values()))
# print("Espera total 2: ", sum(espera2(personas, orden2(personas)).values()))

# print("Sale último: ", sale_ultimo(personas))
# print("Sale último 2: ", sale_ultimo(personas, orden2(personas)))



"""
... Modelo 05 de final ...
Un fabricante de perfumes está intentando crear una nueva fragancia. Desea que la misma sea
del menor costo posible. El perfumista le indicó un listado de ingredientes. Por cada uno de
ellos determinó una cantidad mínima (puede ser cero) y una máxima que debe contar en la
fórmula final. Cada ingrediente tiene asociado un costo por milímetros cúbicos. Conocemos que
la presentación final es de X milímetros cúbicos totales. Presentar una solución utilizando
metodología greedy que resuelva el problema. Analizar la complejidad temporal y espacial.
Probar optimalidad.
"""

ingredientes = {"A": [0, 15], "B": [5, 20], "C": [10, 25], "D": [0, 10], "E": [5, 15], "F": [10, 20]}
costos = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}
x = 50

def agregar_ml_ingrediente(restantes, formula, ml_totales, ingrediente, ml_agregar):
    formula[ingrediente] = formula.get(ingrediente, 0) + ml_agregar
    ml_totales += ml_agregar
    restantes[ingrediente][1] -= ml_agregar
    if restantes[ingrediente][1] == 0:
        del restantes[ingrediente]

def formula(x, ingredientes, costos):
    restantes = ingredientes.copy()
    formula = {}
    ml_totales = 0

    # se pone la cantidad minima de cada ingrediente
    for ingrediente in ingredientes:
        if ingrediente[0] == 0:
            continue
        agregar_ml_ingrediente(restantes, formula, ml_totales, ingrediente, ingredientes[ingrediente][0])
        restantes[ingrediente][0] = 0

    # mientras falte para llegar a x se toma el ingrediente más barato
    while ml_totales < x:
        if len(restantes) == 0:
            print(ml_totales)
            print("No se puede llegar a x")
            return None
        ml_restantes = x - ml_totales
        ingrediente_mas_barato = min(restantes, key=lambda x: costos[x])
        ml_agregar = min(ml_restantes, restantes[ingrediente_mas_barato][1])
        agregar_ml_ingrediente(restantes, formula, ml_totales, ingrediente_mas_barato, ml_agregar)

    return formula

# print("Formula: ", formula(x, ingredientes, costos))

"""
Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P,
por encima del cual se rompen.
- Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos
  comprados, encuentre la mejor forma de distribuir los productos en la menor cantidad
  posible de bolsas.
- Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para
  una lista con los pesos: [ 4, 2, 1, 3, 5 ].
- ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. 
"""

def bolsas_greedy(p, pesos):
    bolsas = []

    for peso in sorted(pesos, reverse=True):
        if len(bolsas) == 0:
            bolsas.append([peso])
            continue

        bolsa_minima = min(bolsas, key=lambda x: sum(x))
        if sum(bolsa_minima) + peso <= p:
            bolsa_minima.append(peso)
        else:
            bolsas.append([peso])

    return bolsas

# print("Bolsas greedy gaga1: ", bolsas_greedy(5, [4, 2, 1, 3, 5]))

def embolsar_greedy(productos, peso_max):
    bolsas = []
    bolsa_actual = []
    for producto in productos:
        if sum(bolsa_actual)+producto < peso_max:
            bolsa_actual.append(producto)
        else:
            bolsas.append(bolsa_actual)
            bolsa_actual = [producto]
    bolsas.append(bolsa_actual)
    return bolsas

# print("Bolsas greedy gaga2: ", embolsar_greedy([4, 2, 1, 3, 5], 5))

ej2 = [5, 4, 3, 2, 2, 2, 2]
from random import shuffle
shuffle(ej2)
print("p = 10, elementos = ", ej2)
print("bolsas_gaga1 = ", bolsas_greedy(10, ej2))
print("bolsas_gaga2 = ", embolsar_greedy(ej2, 10))



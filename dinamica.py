# TODO hacer versión con memoria para cada ejercicio

"""
.. 2 ..
Dado un Grafo dirigido, acíclico G(V, E) con pesos en sus aristas y dos vértices
“s” y “t”; queremos encontrar el camino de mayor peso que exista entre “s” y “t”.
Se pide:
a) Plantear la ecuación de recurrencia
b) Proponer un pseudocódigo para su resolución
c) Determinar la complejidad del algoritmo 
"""

"""
Empiezo en el nodo s, tengo que llegar al nodo t.
s tiene los adyacentes [a1, a2, a3, ..., an], llamo a la función recursiva con cada uno de los adyacentes -> mayor_peso(an, t)
Para cada adyacente, el peso del camino es el peso de la arista + el peso obtenido

pesos = {mayor_peso(a1, t) + peso(a1, t), mayor_peso(a2, t) + peso(a2, t), ..., mayor_peso(an, t) + peso(an, t)}
se devuelve el máximo de los pesos

- Si un nodo no tiene adyacentes, se devuelve -1
- Si un nodo es igual a t, se devuelve 0
"""

from random import shuffle, randint

def antidijkstra(grafo, s, t): # -> O(V + E) (V = vértices, E = aristas) (Implementado como diccionario de diccionarios)
    if s == t:
        return 0, [t]
    
    posibles = {} # {ady: (peso, camino)}
    for ady in grafo.adyacentes(s):
        peso, camino = antidijkstra(grafo, ady, t)
        if peso < 0:
            continue
        peso += grafo.peso(s, ady)
        posibles[ady] = (peso, [s] + camino)

    if len(posibles) == 0:
        return -1, []
    
    maximo = max(posibles.values(), key=lambda x: x[0])
    return maximo

# Usa memoria -> Es dinámica posta

# TODO -> Revisar complejidad y que está bien (me da a robo que sea lineal :sus:)

"""
.. 3 ..
El dueño de una empresa (Charles Fabs) desea organizar una fiesta de la misma. Cómo quiere
que la fiesta sea lo más tranquila posible, no quiere que asistan un empleado y su jefe
directo, pero tampoco quiere que se salteen más de 1 nivel jerárquico. Charles le pidió a
su encargado que le ponga un rating de convivencia (Ri) a cada empleado y con dicha
información más un organigrama de la compañía, le pidió a un especialista en informática
que diseñe un algoritmo para obtener el listado de los empleados que deberá invitar a la
fiesta.
Teniendo en cuenta que: Ri > 0, que Charles no cuenta para el armado del algoritmo y que la
estructura jerárquica es en forma de árbol.
Se pide:
a) Plantear la ecuación de recurrencia
b) Proponer un pseudocódigo para su resolución
c) Determinar la complejidad del algoritmo 
"""

"""
Dado el actual, puedo tenerlo en cuenta o no.
Si lo tengo en cuenta, no puedo tener en cuenta a sus empleados.

Opción 1:
- Lo tengo en cuenta, llamo para los empleados de sus empleados

Opción 2:
- No lo tengo en cuenta, llamo para sus empleados

Siempre me quedo con la opción que me de mayor rating.
"""

def fiesta(organigrama, ratings, lo_tengo_en_cuenta=True):
    if len(organigrama) == 0:
        return 0, []
    
    actual = organigrama.raiz()
    opcion1 = 0
    lista1 = []
    if lo_tengo_en_cuenta:
        for organigrama_empleados in organigrama.hijos(actual):
            peso, lista = fiesta(organigrama_empleados, ratings, False)
            opcion1 += peso
            lista1 += lista
    
    opcion2 = 0
    lista2 = []
    for organigrama_empleados in organigrama.hijos(actual):
        peso, lista = fiesta(organigrama_empleados, ratings, True)
        opcion2 += peso
        lista2 += lista

    if lo_tengo_en_cuenta and opcion1 + ratings[actual] > opcion2:
        return opcion1 + ratings[actual], [actual] + lista1
    
    return opcion2, lista2

# No usa memoria -> Es dinámica trucha
# TODO -> ARREGLAR

"""
... 5 ...
Una agencia de inteligencia ha conseguido interceptar algunos mensajes encriptados de
una agencia rival. Mediante espionaje logran saber algunas cosas para desencriptar los
mensajes. Por ejemplo que para dificultar la tarea de los criptoanalistas los mensajes
enviados no contienen espacios. Se ha organizado un grupo de trabajo para generar un
algoritmo para quebrar la seguridad.
El trabajo se dividió en diferentes partes. A usted le toca dado un string “desencriptado”
y sin espacios determinar si lo que se lee corresponde a un posible mensaje en idioma
castellano. El proceso debe ser rápido dado que se debe utilizar muchasveces.
Cuenta con un diccionario de n palabras y con una cadena de texto con el posible mensaje. 

Ejemplo:
Si el diccionario es “peso”, “pesado”, “oso”, “soso”, “pesa”, “dote”, ”a”, “te”
Para la cadena de texto “osopesadotepesa”
Existe un posible mensaje con las palabras “oso”, “pesado”, “te”, “pesa” 

Para la cadena de texto "ososoapesadote"
No existe un posible mensaje

a) Construir una solución que informe si la cadena de entrada es un posible texto utilizando programación dinámica.
b) plantee el subproblema y la ecuación de recurrencia
c) Analice la complejidad temporal y espacial
d) Existe la posibilidad de que una cadena de texto puede corresponder a más de un mensaje.

Modifique su solución para que se informen todos los posibles mensajes. Determine el impacto en las complejidades en el nuevo algoritmo.
Ejemplo:
La cadena de texto “osopesadote”
Puede corresponder a los mensajes "oso", "pesa”, “dote” u “oso", "pesado", "te"
"""

def prox_palabra_posible(diccionario, cadena, inicio, fin):
    if inicio >= fin:
        raise ValueError("Hacete Scrum Master")
    
    palabra = cadena[:inicio]
    for i in range(inicio, fin):
        palabra += cadena[i]
        if palabra in diccionario:
            return palabra, i + 1
        
    return None, -1

def posible_mensaje_recursivo(diccionario, cadena, min_ini=0):
    if len(cadena) == 0:
        return True
    
    prox_palabra, new_ini = prox_palabra_posible(diccionario, cadena, min_ini, len(cadena))
    if not prox_palabra:
        return False
    
    # si tengo en cuenta la palabra
    if posible_mensaje_recursivo(diccionario, cadena[new_ini:]):
        return True
    
    # si no tengo en cuenta la palabra
    return posible_mensaje_recursivo(diccionario, cadena, new_ini)

# diccionario = {"peso", "pesado", "oso", "soso", "pesa", "dote", "a", "te"}
# cadena = "osopesadotepesa"
# print(posible_mensaje_recursivo(diccionario, cadena))

def posible_mensaje_dinamico(diccionario, cadena):
    if len(cadena) == 0:
        return True
    
    memoria = [False] * len(cadena) # memoria[i] = posible_mensaje(cadena[i:])

    for desde in range(len(cadena) - 1, -1, -1):
        for hasta in range(desde + 1, len(cadena) + 1):
            palabra = cadena[desde:hasta]
            if palabra in diccionario:
                if hasta == len(cadena) or memoria[hasta]:
                    memoria[desde] = True
                    break

    return memoria[0]

# diccionario = {"peso", "pesado", "oso", "soso", "pesa", "dote", "a", "te"}
# cadena = "osopesadopesotepesa"
# print(posible_mensaje_dinamico(diccionario, cadena))

def posibles_mensajes_recursivo(diccionario, cadena, min_ini=0):
    if len(cadena) == min_ini:
        return [[]]
    
    prox_palabra, new_ini = prox_palabra_posible(diccionario, cadena, min_ini, len(cadena))
    if not prox_palabra:
        return []

    # si tengo en cuenta la palabra
    mensajes = posibles_mensajes_recursivo(diccionario, cadena[new_ini:])
    for mensaje in mensajes:
        if len(mensaje) == 0 and len(mensajes) > 1:
            mensajes.remove(mensaje)
        mensaje.append(prox_palabra)
    
    # si no tengo en cuenta la palabra
    mensajes += posibles_mensajes_recursivo(diccionario, cadena, new_ini)

    return mensajes

# diccionario = {"peso", "pesado", "oso", "soso", "pesa", "dote", "a", "te"}
# cadena = "osopesadotepesa"
# print(posibles_mensajes_recursivo(diccionario, cadena))

def posibles_mensajes_dinamico_debug(diccionario, cadena):
    if len(cadena) == 0:
        return [[]]

    memoria = [[] for i in range(len(cadena))] # memoria[i] = posibles_mensajes(cadena[i:])

    for desde in range(len(cadena) - 1, -1, -1):
        print(desde)
        for hasta in range(desde + 1, len(cadena) + 1):
            print("\t", hasta)
            palabra = cadena[desde:hasta]
            if palabra in diccionario:
                print("\t\t", palabra)
                print("\t\t", memoria)
                if hasta == len(cadena):
                    memoria[desde].append([palabra])
                    print("\t\t", memoria[desde])
                    break
                posibles_continuaciones = memoria[hasta]
                memoria[desde] += [[palabra] + posible_continuacion for posible_continuacion in posibles_continuaciones]
                print("\t\t", palabra, memoria[hasta])
                print("\t\t", [[palabra, *posible_continuacion] for posible_continuacion in posibles_continuaciones])

    return memoria[0]

def posibles_mensajes_dinamico(diccionario, cadena):
    if len(cadena) == 0:
        return [[]]

    memoria = [[] for i in range(len(cadena))] # memoria[i] = posibles_mensajes(cadena[i:])

    for desde in range(len(cadena) - 1, -1, -1):
        for hasta in range(desde + 1, len(cadena) + 1):
            palabra = cadena[desde:hasta]

            if palabra in diccionario:
                
                if hasta == len(cadena):
                    memoria[desde] += [[palabra]]
                    break

                posibles_continuaciones = memoria[hasta]
                memoria[desde] += [[palabra] + posible_continuacion for posible_continuacion in posibles_continuaciones]

    return memoria[0]

# diccionario = {"peso", "pesado", "oso", "soso", "pesa", "dote", "a", "te"}
# cadena = "osopesadotepesa"
# print(posibles_mensajes_dinamico(diccionario, cadena))

"""
... 7 ...
Explicar qué representa la ecuación de recurrencia y cuáles son las ventajas
computacionales de resolver un problema utilizando programación dinámica. 
"""

"""
La ecuación de recurrencia representa la relación entre los subproblemas y el
problema original. Es la forma de expresar la solución de un problema en función
de la solución de sus subproblemas.
Las ventajas computacionales de resolver un problema utilizando programación dinámica
son varias. Una de las principales ventajas es la eficiencia, ya que evita volver a
calcular problemas similares varias veces. También es ideal para resolver grandes
problemas de optimización que no serían factibles de resolver con otros métodos.
Además, se evita resolver los mismos subproblemas más de una vez y se evita resolver
subproblemas que no son necesarios para resolver el problema original.
"""

"""
... 9 ...
Contamos con una carretera de longitud M km que tiene distribuidos varios
carteles publicitarios. Cada cartel ”i” está ubicado en un “ki” kilómetro
determinado (pueden ubicarse en cualquier posición o fracción de kilómetro)
y a quien lo utiliza le asegura una ganancia “gi”. Por una regulación no se
puede contratar más de 1 cartel a 5km de otros. Queremos determinar qué
carteles conviene contratar de tal forma de maximizar la ganancia a obtener. 
"""

carteles = [(3.5, 10), (7.0, 3), (8.75, 10), (10.5, 6), (17.5, 1)] # (ki, gi)

def prox_cartel(carteles, ult_cartel=-5):
    for i in range(len(carteles)):
        if carteles[i][0] >= ult_cartel + 5:
            return i
    return None

def suma_carteles(carteles):
    suma = 0
    for cartel in carteles:
        suma += cartel[1]
    return suma

def carteles_optimos_recursivo(carteles, ult_cartel=-5):
    carteles.sort(key=lambda x: x[0])
    
    index = prox_cartel(carteles, ult_cartel)
    if index is None:
        return []
    
    primero = carteles[index]
    if index == len(carteles) - 1:
        return [primero]

    resto = carteles[index + 1:]
    
    # si tengo en cuenta el primer cartel
    optimos1 = carteles_optimos_recursivo(resto, primero[0])
    optimos1.insert(0, primero)

    # si no tengo en cuenta el primer cartel
    optimos2 = carteles_optimos_recursivo(resto, ult_cartel)
    
    if suma_carteles(optimos1) > suma_carteles(optimos2):
        return optimos1
    return optimos2

# print(carteles_optimos_recursivo(carteles))

def carteles_optimos_dinamico(carteles):
    carteles.sort(key=lambda x: x[0])
    
    memoria = [[] for i in range(len(carteles))] # memoria[i] = carteles_optimos(carteles[i:])
    memoria[0] = [carteles[0]]

    for i in range(1, len(carteles)):
        cartel = carteles[i]

        # si hay más de 5km entre el cartel actual y el anterior
        # ponemos todos los carteles anteriores y el actual
        if cartel[0] >= memoria[i - 1][-1][0] + 5:
            memoria[i] = memoria[i - 1] + [cartel]
            continue

        # si no, vemos si conviene poner el cartel actual
        # o conviene no ponerlo
        ult_opcion_posible = None
        for j in range(i - 1, -1, -1):
            if cartel[0] >= memoria[j][-1][0] + 5:
                ult_opcion_posible = j
                break
        opcion1 = memoria[ult_opcion_posible] + [cartel] if ult_opcion_posible is not None else [cartel]
        opcion2 = memoria[i - 1]
        memoria[i] = opcion1 if suma_carteles(opcion1) > suma_carteles(opcion2) else opcion2

    return memoria[-1]

# print(carteles_optimos_dinamico(carteles))

"""
... Modelo 01 de final ...
Una empresa que realiza ciencia de datos debe realizar en las próximas “n” semanas
procesos y cálculos intensivos. Para eso debe contratar tiempo de cómputo en un data
center. Realizando una estimación conocen cuantas horas de cómputo necesitarán para
cada una de las semanas. Por otro lado luego de negociar con los principales
proveedores tienen 2 opciones que pueden combinar a gusto:
● Opción 1: Contratar a la empresa “Arganzón” por semana. En esa semana se cobra
  proporcional al tiempo de cómputo según un parámetro “r”  (horas computo x r).
● Opción 2: Contratar a la empresa “Fuddle” por un lapso de 3 semanas contiguas.
  Durante el lapso contratado se paga una tarifa fija de “c”.

Proponer una solución utilizando programación dinámica que nos indique la secuencia de
elecciones a realizar para minimizar el costo total de cómputo. Analizar su complejidad
temporal y espacial. 
"""

def contratar_recursivo(weeks, r, c):
    if len(weeks) == 0:
        return 0, []
    
    # si contrato a Arganzón
    opcion1 = contratar_recursivo(weeks[1:], r, c)
    costo1 = opcion1[0] + weeks[0] * r
    
    # si contrato a Fuddle
    opcion2 = float("inf"), []
    if len(weeks) >= 3:
        opcion2 = contratar_recursivo(weeks[3:], r, c)
    costo2 = opcion2[0] + c
    
    if costo1 < costo2:
        return costo1, ["A"] + opcion1[1]
    return costo2, ["FFF"] + opcion2[1]

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# r = 1
# c = 10
# print(array)
# print(contratar_recursivo(array, r, c))
# shuffle(array)
# print(array)
# print(contratar_recursivo(array, r, c))
# shuffle(array)
# print(array)
# print(contratar_recursivo(array, r, c))

def contratar_dinamico(weeks, r, c):
    if len(weeks) == 0:
        return 0, []
    
    memoria = [(0, []) for i in range(len(weeks))] # memoria[i] = contratar(weeks[i:], r, c)

    for i in range(len(weeks)):
        semana = weeks[i]

        # si contrato a Arganzón
        opcion1 = memoria[i - 1] if i > 0 else (0, [])
        costo1 = opcion1[0] + semana * r

        # si contrato a Fuddle
        opcion2 = (float("inf"), [])
        if i >= 2:
            opcion2 = memoria[i - 3] if i - 3 >= 0 else (0, [])
        costo2 = opcion2[0] + c

        if costo1 < costo2:
            memoria[i] = costo1, opcion1[1] + ["A"] 
        else:
            memoria[i] = costo2, opcion2[1] + ["FFF"]

    return memoria[-1]

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# r = 1
# c = 10
# print(array)
# print(contratar_recursivo(array, r, c))
# print(contratar_dinamico(array, r, c))
# shuffle(array)
# print(array)
# print(contratar_recursivo(array, r, c))
# print(contratar_dinamico(array, r, c))
# shuffle(array)
# print(array)
# print(contratar_recursivo(array, r, c))
# print(contratar_dinamico(array, r, c))
# array = [1, 3, 1, 1, 1, 10, 10, 10, 9, 8, 4, 8, 3, 4, 1]
# r = 3
# c = 15
# print(array)
# print(contratar_recursivo(array, r, c))
# print(contratar_dinamico(array, r, c))
# shuffle(array)
# print(array)
# print(contratar_recursivo(array, r, c))
# print(contratar_dinamico(array, r, c))
# shuffle(array)
# print(array)
# print(contratar_recursivo(array, r, c))
# print(contratar_dinamico(array, r, c))
# random_array = [randint(1, 10) for i in range(15)]
# r = randint(1, 5)
# c = randint(10, 20)
# print(array)
# print(contratar_recursivo(array, r, c))
# print(contratar_dinamico(array, r, c))
# shuffle(array)
# print(array)
# print(contratar_recursivo(array, r, c))
# print(contratar_dinamico(array, r, c))
# shuffle(array)
# print(array)
# print(contratar_recursivo(array, r, c))
# print(contratar_dinamico(array, r, c))

# funciones para verificar
def generar_combinaciones(weeks, r, c):
    if len(weeks) == 0:
        return []
    
    # si contrato a Arganzón
    opcion1 = generar_combinaciones(weeks[1:], r, c)
    combinaciones1 = []
    for opcion in opcion1:
        combinaciones1.append(["A"] + opcion)
    if len(combinaciones1) == 0:
        combinaciones1.append(["A"])
    
    # si contrato a Fuddle
    opcion2 = []
    if len(weeks) >= 3:
        opcion2 = generar_combinaciones(weeks[3:], r, c)
    combinaciones2 = []
    for opcion in opcion2:
        combinaciones2.append(["FFF"] + opcion)
    if len(combinaciones2) == 0:
        combinaciones2.append(["FFF"])

    return combinaciones1 + combinaciones2

def costos_combinaciones(weeks, r, c):
    combinaciones = generar_combinaciones(weeks, r, c)
    costos = []
    for combinacion in combinaciones:
        costo = 0
        for i in range(len(combinacion)):
            if combinacion[i] == "A":
                costo += weeks[i] * r
            else:
                costo += c
        costos.append(costo)
    return costos

def min_costo(weeks, r, c):
    costos = costos_combinaciones(weeks, r, c)
    minimo = min(costos)
    return minimo, costos.index(minimo)

# print(min_costo([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 10))

"""
... Modelo 02 de final ...
Se conoce como “Longest increasing subsequences” al problema de encontrar la subsecuencia
más larga de números (no necesariamente consecutivos) donde cada elemento sea mayor a los
anteriores en una secuencia de números.

Ejemplo:
    En la lista →  2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7.
    Podemos ver que la subsecuencia más larga es de longitud 6 y corresponde a la siguiente
    “2, *1*, 4, *2*, *3*, 9, *4*, 6, *5*, 4, *7*”

Este problema se puede resolver de varias maneras. Entre ellas, utilizando programación
dinámica.
Se pide: resolverlo mediante programación dinámica. Usar el ejemplo del enunciado para
explicar paso a paso el método. 
"""

array = [2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7]

def longest_increblahblah_recursivo(array, minimo=0):
    if len(array) == 0:
        return []

    # tomo el primer elemento que sea mayor al minimo
    menores = [i for i in range(len(array)) if array[i] > minimo]
    if len(menores) == 0:
        return []
    primero = min(menores)
    
    # si tengo en cuenta el primero
    opcion1 = [array[primero]] + longest_increblahblah_recursivo(array[primero + 1:], array[primero])

    # si no tengo en cuenta el primero
    opcion2 = longest_increblahblah_recursivo(array[primero + 1:], minimo)

    return opcion1 if len(opcion1) > len(opcion2) else opcion2

# print(longest_increblahblah_recursivo(array))
from copy import deepcopy
def longest_increblahblah_dinamico(array):
    if len(array) == 0:
        return []
    
    memoria = [[] for i in range(len(array))] # memoria[i] = longest_increblahblah(array[i:])
    memoria[0] = [array[0]]

    for i in range(1, len(array)):
        numero = array[i]

        # si el último numero es menor al actual
        # ponemos la secuencia anterior y el actual
        if memoria[i - 1][-1] < numero:
            memoria[i] = memoria[i - 1] + [numero]
            continue

        # si no, vemos si conviene poner el numero actual
        # o conviene no ponerlo
        ult_opcion_posible = None
        opciones = deepcopy(memoria[:i - 1])
        # se ordenan las opciones
        # 1° criterio: longitud
        # 2° criterio (desempate): último número más chico
        opciones.sort(key=lambda x: (len(x), x[-1]))
        for j in range(len(opciones) - 1, -1, -1):
            if opciones[j][-1] < numero:
                ult_opcion_posible = memoria.index(opciones[j])
                break
        opcion1 = memoria[ult_opcion_posible] + [numero] if ult_opcion_posible is not None else [numero]
        opcion2 = memoria[i - 1]
        
        if len(opcion1) > len(opcion2):  # feo pero funca ._.
            memoria[i] = opcion1
        elif len(opcion1) < len(opcion2):
            memoria[i] = opcion2
        elif opcion1[-1] < opcion2[-1]:
            memoria[i] = opcion1
        else:
            memoria[i] = opcion2

    return memoria[-1]

# print(longest_increblahblah_dinamico(array))

"""
... Modelo 04 de final ...
Recordemos al problema 2-Partition: Se cuenta con un conjunto de “n” elementos.
Cada uno de ellos tiene un valor asociado. Se desea separar los elementos en 2
conjuntos que cumplan con: La suma de los valores de cada conjunto sea igual
entre ellos. Se puede ver que este corresponde a un problema NP-C. Sin embargo
- al igual que otros problemas en esta clase como el problema de la mochila -
puede ser resuelto utilizando programación dinámica.

Proponga un algoritmo utilizando programación dinámica que resuelva cualquier
instancia de 2-Partition. Analice su complejidad temporal y espacial. 
"""

def _two_partition_recursivo(array, partitions):
    if len(array) == 0:
        return partitions
    
    # si lo agrego al primer conjunto
    opcion1 = partitions[0] + [array[0]], partitions[1]
    opcion1 = _two_partition_recursivo(array[1:], opcion1)
    if opcion1[0] == opcion1[1]:
        return opcion1

    # si lo agrego al segundo conjunto
    opcion2 = partitions[0], partitions[1] + [array[0]]
    opcion2 = _two_partition_recursivo(array[1:], opcion2)
    
    if abs(sum(opcion1[0]) - sum(opcion1[1])) < abs(sum(opcion2[0]) - sum(opcion2[1])):
        return opcion1
    return opcion2

def two_partition_recursivo(array):
    partitions = _two_partition_recursivo(array, ([], []))
    print(partitions)
    return True if sum(partitions[0]) == sum(partitions[1]) else False

array = [3, 1, 1, 2, 2, 1]
# print(two_partition_recursivo(array))
# shuffle(array)
# print(two_partition_recursivo(array))

# No usa memoria -> Es dinámica trucha
# TODO -> ARREGLAR

"""
... Modelo 05 de final ...
El dueño de una cosechadora está teniendo una demanda muy elevada en los próximos
3 meses. Desde “n” campos lo quieren contratar para que preste sus servicios.
Lamentablemente no puede hacer todos los contratos puesto que varios de ellos se
superponen en sus tiempos. Cuenta con un listado de los pedidos donde para cada uno
de ellos se consigna: fecha de inicio, fecha de finalización, monto a ganar por
realizarlo. Su idea es seleccionar la mayor cantidad de trabajos posibles. Por eso
seleccionará primero aquellos trabajos que le demanden menos tiempo. Mostrarle que
esta solución puede no ser la óptima. Proponer una solución utilizando programación
dinámica que nos otorgue el resultado óptimo. Analizar su complejidad temporal y
espacial.
"""

ofertas = [(0, 5, 10), (0, 3, 5), (4, 6, 7), (5, 7, 8), (6, 10, 9), (8, 10, 10), (9, 10, 11)] # (inicio, fin, monto)

def mejor_plan_recursivo(ofertas):
    # se ordenan las ofertas
    # - 1° criterio: fecha de inicio
    # - 2° criterio (desempate): fecha de fin
    ofertas.sort(key=lambda x: (x[0], x[1]))
    
    return _mejor_plan_recursivo(ofertas)

def _mejor_plan_recursivo(ofertas):
    if len(ofertas) == 0:
        return 0, []
    
    primera = ofertas[0]

    # si tomo la primera
    # elimino las ofertas que se superponen con la primera
    filtradas = [oferta for oferta in ofertas if oferta[0] >= primera[1]]
    opcion1 = _mejor_plan_recursivo(filtradas)
    opcion1 = (opcion1[0] + primera[2], [primera] + opcion1[1])

    # si no tomo la primera
    resto = ofertas[1:]
    opcion2 = _mejor_plan_recursivo(resto)

    return opcion1 if opcion1[0] > opcion2[0] else opcion2

def mejor_plan_dinamico(ofertas):
    if len(ofertas) == 0:
        return 0, []
    
    ofertas.sort(key=lambda x: (x[0], x[1]))
    memoria = [(0, []) for i in range(len(ofertas))] # memoria[i] = mejor_plan(ofertas[i:])
    memoria[0] = ofertas[0][2], [ofertas[0]]

    for i in range(1, len(ofertas)):
        oferta = ofertas[i]

        # si la oferta actual no se superpone con la anterior
        # ponemos la oferta anterior y la actual
        if oferta[0] >= memoria[i - 1][1][-1][1]:
            memoria[i] = memoria[i - 1][0] + oferta[2], memoria[i - 1][1] + [oferta]
            continue

        # si no, vemos si conviene poner la oferta actual
        # o conviene no ponerla
        ult_opcion_posible = None
        for j in range(i - 1, -1, -1):
            if oferta[0] >= memoria[j][1][-1][1]:
                ult_opcion_posible = j
                break
        opcion1 = oferta[2], [oferta]
        if ult_opcion_posible is not None:
            opcion1 = memoria[ult_opcion_posible][0] + oferta[2], memoria[ult_opcion_posible][1] + [oferta]
        
        opcion2 = memoria[i - 1]
        memoria[i] = opcion1 if opcion1[0] > opcion2[0] else opcion2

    return memoria[-1]

# versión greedy que elige la oferta que elige las ofertas que demandan menos tiempo
def posible(oferta, seleccionadas):
    for seleccionada in seleccionadas:
        if oferta[0] >= seleccionada[1] or oferta[1] <= seleccionada[0]:
            continue
        return False
    return True

def mejor_plan_greedy(ofertas):
    ofertas.sort(key=lambda x: x[1] - x[0])
    seleccionadas = []
    for oferta in ofertas:
        if len(seleccionadas) == 0:
            seleccionadas.append(oferta)
            continue
        if posible(oferta, seleccionadas):
            seleccionadas.append(oferta)
    return sum([oferta[2] for oferta in seleccionadas]), seleccionadas

# print(mejor_plan_greedy(ofertas))
# print(mejor_plan_recursivo(ofertas))
# print(mejor_plan_dinamico(ofertas))

def juan_el_vago_escondido(lista):
    if len(lista) == 0:
        return []
    if len(lista) == 1:
        return [lista[0]]

    memoria = [[] for _ in range(len(lista))]
    memoria[0] = [lista[0]]
    memoria[1] = [lista[1]]

    for i in range(2, len(lista)):
        elemento = lista[i]
        
        # opción 1 -> contar el elemento
        # agarro la mejor sol sin tener en cuenta al anterior (memoria[i - 2])
        opcion1 = memoria[i - 2] + [elemento]
        
        # opción 2 -> no contar el elemento
        # agarro la mejor sol (memoria[i - 1])
        opcion2 = memoria[i - 1]
        
        # me quedo con el  que maximice
        memoria[i] = opcion1 if sum(opcion1) > sum(opcion2) else opcion2
    
    return memoria[-1]

lista = [8, 12, 13, 24, 55, 26, 37]

# print(lista)
# print(juan_el_vago_escondido(lista))

"""
1.
Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta
que anota los grupos que quieren sentarse a comer, y la cantidad de integrantes
que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P
donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en
total n grupos. Como se trata de un restaurante familiar, las personas sólo se
sientan en la mesa si todos los integrantes de su grupo pueden sentarse.
Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto
de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras,
que dejan la menor cantidad de espacios vacíos).
Indicar y justificar la complejidad del algoritmo. 
"""

def mesa_w(w, grupos):
    ocupados, sum_ocupados = [], 0
    ocupados_ant, sum_ocupados_ant = [], 0
    
    for i in range(len(grupos)):
        cant_integrantes = grupos[i]
        if cant_integrantes > w:
            continue

        if sum_ocupados + cant_integrantes <= w:
            ocupados.append(cant_integrantes)
            sum_ocupados += cant_integrantes
            continue

        # opción 1 -> tenerlo en cuenta
        opcion1, sum_opcion1 = [cant_integrantes], cant_integrantes
        if sum_ocupados_ant + cant_integrantes <= w:
            opcion1 = ocupados_ant + [cant_integrantes]
            sum_opcion1 = sum_ocupados_ant + cant_integrantes

        # opción 2 -> no tenerlo en cuenta
        opcion2, sum_opcion2 = ocupados, sum_ocupados

        # me quedo con el que maximice
        ocupados_ant, sum_ocupados_ant = ocupados[:], sum_ocupados
        ocupados, sum_ocupados = opcion1, sum_opcion1
        if sum_opcion1 < sum_opcion2:
            ocupados, sum_ocupados = opcion2, sum_opcion2

    return ocupados

op_mayor_grupo = randint(1, 25)
cant_grupos = randint(1, 25) + 5

# grupos = [randint(1, op_mayor_grupo) for i in range(cant_grupos)]
# print(f"op_mayor_grupo: {op_mayor_grupo}\ncant_grupos: {cant_grupos}\ngrupos: {grupos}")
# diferencias = []
# for i in range(0, sum(grupos) + 1):
#     mesa = mesa_w(i, grupos)
#     # print(mesa, i, sum(mesa))
#     diferencias.append(i - sum(mesa))
# print(diferencias)

"""
3.
Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una
suma de cuadrados, utilizando programación dinámica. Indicar y justificar el orden del algoritmo
implementado. Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1^2,
por lo que siempre existe solución.
Sin embargo, la expresión 10 = 3^2 + 1^2 es una manera más económica de escribirlo para n = 10,
pues sólo tiene dos términos. Además, tener en cuenta que no se piden los términos, sino la cantidad
mínima de términos cuadráticos necesaria. 
"""


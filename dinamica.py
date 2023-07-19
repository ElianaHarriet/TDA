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

from random import shuffle


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

def posible_mensaje(diccionario, cadena, min_ini=0):
    if len(cadena) == 0:
        return True
    
    prox_palabra, new_ini = prox_palabra_posible(diccionario, cadena, min_ini, len(cadena))
    if not prox_palabra:
        return False
    
    # si tengo en cuenta la palabra
    if posible_mensaje(diccionario, cadena[new_ini:]):
        print(prox_palabra)
        return True
    
    # si no tengo en cuenta la palabra
    return posible_mensaje(diccionario, cadena, new_ini)

# diccionario = {"peso", "pesado", "oso", "soso", "pesa", "dote", "a", "te"}
# cadena = "osopesadotepesa"
# print(posible_mensaje(diccionario, cadena))

def posibles_mensajes(diccionario, cadena, min_ini=0):
    if len(cadena) == min_ini:
        return [[]]
    
    prox_palabra, new_ini = prox_palabra_posible(diccionario, cadena, min_ini, len(cadena))
    if not prox_palabra:
        return []

    # si tengo en cuenta la palabra
    mensajes = posibles_mensajes(diccionario, cadena[new_ini:])
    for mensaje in mensajes:
        if len(mensaje) == 0 and len(mensajes) > 1:
            mensajes.remove(mensaje)
        mensaje.append(prox_palabra)
    
    # si no tengo en cuenta la palabra
    mensajes += posibles_mensajes(diccionario, cadena, new_ini)

    return mensajes

# diccionario = {"peso", "pesado", "oso", "soso", "pesa", "dote", "a", "te"}
# cadena = "osopesadotepesa"
# print(posibles_mensajes(diccionario, cadena))
    

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

def carteles_optimos(carteles, ult_cartel=-5):
    carteles.sort(key=lambda x: x[0])
    
    index = prox_cartel(carteles, ult_cartel)
    if index is None:
        return []
    
    primero = carteles[index]
    if index == len(carteles) - 1:
        return [primero]

    resto = carteles[index + 1:]
    
    # si tengo en cuenta el primer cartel
    optimos1 = carteles_optimos(resto, primero[0])
    optimos1.insert(0, primero)

    # si no tengo en cuenta el primer cartel
    optimos2 = carteles_optimos(resto, ult_cartel)
    
    if suma_carteles(optimos1) > suma_carteles(optimos2):
        return optimos1
    return optimos2

# print(carteles_optimos(carteles))

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

def contratar(weeks, r, c):
    if len(weeks) == 0:
        return 0, []
    
    # si contrato a Arganzón
    opcion1 = contratar(weeks[1:], r, c)
    costo1 = opcion1[0] + weeks[0] * r
    
    # si contrato a Fuddle
    opcion2 = float("inf"), []
    if len(weeks) >= 3:
        opcion2 = contratar(weeks[3:], r, c)
    costo2 = opcion2[0] + c
    
    if costo1 < costo2:
        return costo1, ["A"] + opcion1[1]
    return costo2, ["FFF"] + opcion2[1]

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# r = 1
# c = 10
# print(array)
# print(contratar(array, r, c))
# shuffle(array)
# print(array)
# print(contratar(array, r, c))
# shuffle(array)
# print(array)
# print(contratar(array, r, c))

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
Se conoce como “Longest increasing subsequences” al problema de encontrar la
subsecuencia más larga de números (no necesariamente consecutivos) donde cada
elemento sea mayor a los anteriores en una secuencia de números.

Ejemplo:
En la lista →  2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7.
Podemos ver que la subsecuencia más larga es de longitud 6 y corresponde a la
siguiente (marcada en negrita) “2, **1**, 4, **2**, **3**, 9, **4**, 6, **5**, 4, **7**”

Este problema se puede resolver de varias maneras. Entre ellas, utilizando
programación dinámica. Se pide: resolverlo mediante programación dinámica.
Usar el ejemplo del enunciado para explicar paso a paso el método. 
"""

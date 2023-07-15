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


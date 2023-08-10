"""
5.
Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta la
capacidad a una artista, permita obtener el nuevo flujo máximo en tiempo lineal en
vértices y aristas. Indicar y justificar la complejidad del algoritmo implementado. 
"""

from collections import deque


def bfs(grafo, origen, destino): # O(V + E)
    visitados = set()
    padres = {}
    cola = deque()

    visitados.add(origen)
    padres[origen] = None
    cola.append(origen)

    while cola:
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                padres[w] = v
                cola.append(w)
                if w == destino:
                    return padres
    return None

def obtener_aumento(red_residual, fuente, sumidero, peso_vw, padres): # O(V)
    aumento = peso_vw
    actual = sumidero
    while actual != fuente:
        padre = padres[actual]
        posible_aumento = red_residual.peso_arista(padre, actual)
        if posible_aumento < aumento:
            aumento = posible_aumento
        actual = padre
    return aumento

def actualizar_flujo(red_residual, fuente, sumidero, padres, aumento): # O(V)
    w = sumidero
    while w != fuente:
        v = padres[w]
        peso_vw = red_residual.peso_arista(v, w)
        peso_wv = red_residual.peso_arista(w, v)
        red_residual.actualizar_peso_arista(v, w, peso_vw - aumento)
        red_residual.actualizar_peso_arista(w, v, peso_wv + aumento)
        w = v

def aumentar_flujo(arista, red_residual, fuente, sumidero): # O(V + E)
    v, w, peso = arista
    peso_wv = red_residual.peso_arista(w, v)
    peso_vw = peso - peso_wv
    if peso_vw <= 0:
        return False
    red_residual.actualizar_peso_arista(v, w, peso_vw) # O(1)

    padres = bfs(red_residual, fuente, sumidero) # O(V + E)
    if padres is None:
        return False
    
    aumento = obtener_aumento(red_residual, fuente, sumidero, peso_vw, padres) # O(V)
    if aumento <= 0:
        return False
    
    actualizar_flujo(red_residual, fuente, sumidero, padres, aumento) # O(V)
    return True
        
"""
Carlos tiene un problema: sus 5 hijos no se soportan. Esto es a tal punto, que ni
siquiera están dispuestos a caminar juntos para ir a la escuela. Incluso más:
¡tampoco quieren pasar por una cuadra por la que haya pasado alguno de sus hermanos!
Sólo aceptan pasar por las esquinas, si es que algún otro pasó por allí. Por suerte,
tanto la casa como la escuela quedan en esquinas, pero no está seguro si es posible
enviar a sus 5 hijos a la misma escuela. Utilizando lo visto en la materia, formular
este problema y resolverlo. Indicar y justificar la complejidad del algoritmo. 
"""

def ford_fulkerson(grafo, fuente, sumidero): # O(V * E^2)
    red_residual = grafo.copy()
    
    while True:
        padres = bfs(red_residual, fuente, sumidero) # O(V + E)
        if not padres:
            break
        aumento = obtener_aumento(red_residual, fuente, sumidero, float('inf'), padres) # O(V)
        actualizar_flujo(red_residual, fuente, sumidero, padres, aumento) # O(V)
    
    return red_residual

def k_hijos_posibles(grafo_ciudad, casa, escuela, k):
    red_residual = ford_fulkerson(grafo_ciudad, casa, escuela) # O(V * E) por ser el problema de caminos disjuntos
    flujo = 0
    for v in red_residual.adyacentes(casa):
        if red_residual.estan_unidos(v, casa):
            flujo += red_residual.peso_arista(v, casa)
    return flujo >= k

    
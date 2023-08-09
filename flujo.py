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
        
    

    
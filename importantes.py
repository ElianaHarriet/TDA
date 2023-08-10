# No fueron testeados

"""
Independent set - backtracking
"""

def independiente(grafo, iset, v):
    for w in iset:
        if v in grafo.obtener_adyacentes(w):
            return False
    return True

def _independet_set_backtracking(grafo, k, iset, restantes):
    v = None
    while not independiente(grafo, iset, v) and len(restantes) > 0:
        v = restantes.pop()
    if not v:
        return None
    
    iset.append(v)
    if len(iset) == k:
        return iset
    if len(restantes) + len(iset) < k:
        return None
    
    if _independet_set_backtracking(grafo, k, iset, restantes):
        return iset
    iset.pop()
    return _independet_set_backtracking(grafo, k, iset, restantes)

def independet_set_backtracking(grafo, k):
    return _independet_set_backtracking(grafo, k, [], grafo.obtener_vertices())

"""
Independet set - dinámica
"""

def independet_set_dinamica(grafo, k):
    vertices = grafo.obtener_vertices()

    memoria = [[] for _ in range(len(vertices))]
    memoria[0] = [vertices[0]]

    for i in range(1, len(vertices)):
        if len(memoria[i - 1]) == k:
            return memoria[i - 1]
        
        v = vertices[i]
        
        if independiente(grafo, memoria[i - 1], v):
            memoria[i] = memoria[i - 1] + [v]
            continue

        # opción 1: agregar v
        op1 = [v]
        for j in range(i - 1, -1, -1):
            if independiente(grafo, memoria[j], v):
                op1 += memoria[j][:]
                break
        
        # opción 2: no agregar v
        op2 = memoria[i - 1][:]

        memoria[i] = op1 if len(op1) > len(op2) else op2

    return memoria[-1]

"""
Vertex cover - backtracking
"""

def _vertex_cover_backtracking(grafo, k, cover, restantes):
    if len(restantes) == 0:
        return cover if len(cover) <= k else None
    
    if len(cover) == k:
        for rest in restantes:
            if rest[0] not in cover and rest[1] not in cover:
                return None
    
    v, w, _ = restantes.pop() # (v, w, peso)
    if v in cover or w in cover:
        return _vertex_cover_backtracking(grafo, k, cover, restantes)
    
    cover.append(v)
    if _vertex_cover_backtracking(grafo, k, cover, restantes):
        return cover
    
    cover.pop()
    cover.append(w)
    return _vertex_cover_backtracking(grafo, k, cover, restantes)

def vertex_cover_backtracking(grafo, k):
    return _vertex_cover_backtracking(grafo, k, [], grafo.obtener_aristas())

"""
Vertex cover - dinámica
"""

# TODO

"""
K clique - backtracking
"""
# Clique -> subgrafo completo

def _k_clique_backtracking(grafo, k, clique, restantes):
    if len(clique) == k:
        return clique
    
    if len(restantes) + len(clique) < k:
        return None
    
    v = None
    while not v and len(restantes) > 0:
        v = restantes.pop()
        for w in clique:
            if w not in grafo.obtener_adyacentes(v):
                v = None
    
    if not v:
        return None
    
    clique.append(v)
    if _k_clique_backtracking(grafo, k, clique, restantes):
        return clique
    
    clique.pop()
    return _k_clique_backtracking(grafo, k, clique, restantes)

def k_clique_backtracking(grafo, k):
    return _k_clique_backtracking(grafo, k, [], grafo.obtener_vertices())

"""
K clique - dinámica
"""

def full_conectado(grafo, clique, v):
    for w in clique:
        if w not in grafo.obtener_adyacentes(v):
            return False
    return True

def k_clique_dinamica(grafo, k):
    vertices = grafo.obtener_vertices()

    memoria = [[] for _ in range(len(vertices))]
    memoria[0] = [vertices[0]]

    for i in range(1, len(vertices)):
        if len(memoria[i - 1]) == k:
            return memoria[i - 1]
        
        v = vertices[i]
        
        if full_conectado(grafo, memoria[i - 1], v):
            memoria[i] = memoria[i - 1] + [v]
            continue

        # opción 1: agregar v
        op1 = [v]
        for j in range(i - 1, -1, -1):
            if full_conectado(grafo, memoria[j], v):
                op1 += memoria[j][:]
                break

        # opción 2: no agregar v
        op2 = memoria[i - 1][:]

        memoria[i] = op1 if len(op1) > len(op2) else op2

    return memoria[-1]

"""
Camino hamiltoniano - backtracking
"""
# Camino hamiltoniano -> camino que recorre todos los vértices
#                       del grafo sin repetir ninguno y luego vuelve al inicial

def _camino_hamiltoniano_backtracking(grafo, camino, restantes):
    if len(restantes) == 0:
        return camino if camino[0] in grafo.obtener_adyacentes(camino[-1]) else None
    
    v = camino[-1]
    for w in grafo.obtener_adyacentes(v):
        if w in camino:
            continue   

        camino.append(w)
        if _camino_hamiltoniano_backtracking(grafo, camino, restantes - {w}):
            return camino
        camino.pop()

    return None

def camino_hamiltoniano_backtracking(grafo):
    for v in grafo.obtener_vertices():
        camino = [v]
        if _camino_hamiltoniano_backtracking(grafo, camino, set(grafo.obtener_vertices()) - {v}):
            return camino
    return None

"""
Camino hamiltoniano - dinámica
"""

# TODO

"""
Subset sum - Backtracking
"""

def _subset_sum_backtracking(suma, subconjunto, restantes):
    if sum(subconjunto) == suma:
        return subconjunto
    if sum(restantes) + sum(subconjunto) < suma:
        return None
    
    v = restantes.pop()
    subconjunto.append(v)
    if _subset_sum_backtracking(suma, subconjunto, restantes):
        return subconjunto
    subconjunto.pop()
    return _subset_sum_backtracking(suma, subconjunto, restantes)

def subset_sum_backtracking(conjunto, suma):
    return _subset_sum_backtracking(suma, [], conjunto[:])

"""
Subset sum - Dinámica
"""

# TODO



    


        

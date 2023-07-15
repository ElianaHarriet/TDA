def _soborno_dinamico(existencias, pedido):
    if len(existencias) == 1:
        return existencias
    
    elemento = existencias[0]
    elementos_restantes = existencias[1:]
    total_restante = sum(elementos_restantes)

    # considerando el elemento
    restante = pedido - elemento
    if restante == 0:
        return [elemento]
    if total_restante < restante:
        return None
    soborno_restante = _soborno_dinamico(elementos_restantes, restante)

    # sin considerar el elemento
    if total_restante < pedido:
        return [elemento] + soborno_restante
    soborno_sin_elemento = _soborno_dinamico(elementos_restantes, pedido)

    # if soborno_restante is None:
    #     return soborno_sin_elemento
    # if soborno_sin_elemento is None: # por qué pasaría?! pero por las dudas
    #     return [elemento] + soborno_restante
    
    total_con_elemento = sum([elemento] + soborno_restante)
    total_sin_elemento = sum(soborno_sin_elemento)
    if total_con_elemento < total_sin_elemento:
        return [elemento] + soborno_restante
    return soborno_sin_elemento
    


def soborno_dinamico(existencias, pedido):
    soborno = {}
    for tipo in pedido.keys():
        soborno[tipo] = _soborno_dinamico(existencias[tipo], pedido[tipo])
    return soborno

pedido = {"creditos_fiuba": 6}
existencias = {"creditos_fiuba": [1, 2, 3, 5, 7]}
print(soborno_dinamico(existencias, pedido))

pedido = {"creditos_fiuba": 9}
existencias = {"creditos_fiuba": [1, 2, 3, 5, 7]}
print(soborno_dinamico(existencias, pedido))

pedido = {"creditos_fiuba": 11}
existencias = {"creditos_fiuba": [1, 1, 5, 6, 9]}
print(soborno_dinamico(existencias, pedido))
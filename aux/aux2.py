def knapsack_problem_items(values, weights, n, W):
    m = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(W + 1):
            if weights[i-1] > j:
                m[i][j] = m[i-1][j]
            else:
                m[i][j] = max(m[i-1][j], m[i-1][j-weights[i-1]] + values[i-1])

    # now we backtrack to find the items
    items = []
    i = n
    j = W
    while i > 0 and j > 0:
        if m[i][j] != m[i-1][j]:
            items.append(values[i-1])
            j -= weights[i-1]
        i -= 1
    return items


def _soborno_dinamico(existencias, pedido):
    values = existencias
    weights = existencias
    n = len(existencias)
    W = sum(existencias) - pedido
    me_quedo = knapsack_problem_items(values, weights, n, W)
    soborno = []
    for i in existencias:
        if i not in me_quedo:
            soborno.append(i)
    return soborno

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





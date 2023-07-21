"""
.. 2 ..
Un colaborador del laboratorio de “cálculo automatizado S.A” propone un nuevo método de
multiplicación de matrices. Utiliza división y conquista partiendo la matrices en bloques
de tamaño n/4 x n/4. Y el proceso de combinación de resultados llevara Θ(n^2). Se muestra
vago en indicar la cantidad de subproblemas que creará cada paso. Le indican que este dato
es fundamental para decidir si proseguir con esa línea de investigación o no. Actualmente
utilizan el algoritmo de Strassen con una complejidad de O(n^log_2(7)).
Siendo T(n) = aT (n/4) + Θ(n^2), con a la información a determinar. ¿Cuál es la cantidad
de subproblemas más grande que puede tomar la solución para que sea mejor que su algoritmo
actual? 
"""

"""
Teorema maestro:
T(n) = aT(n/b) + f(n^c)

            < c -> T(n) = Θ(n^c)
log_b(a)    = c -> T(n) = Θ(n^c log(n))
            > c -> T(n) = Θ(n^log_b(a))

O(n^log_2(7)) = O(n^2.8074)

T(n) = aT (n/4) + Θ(n^2)

            < c -> T(n) = Θ(n^2)            -> mejor que O(n^log_2(7))                  (caso a)
log_4(a)    = c -> T(n) = Θ(n^2 log(n))     -> mejor que O(n^log_2(7))                  (caso b)
            > c -> T(n) = Θ(n^log_4(a))     -> mejor siempre que log_4(a) < log_2(7)    (caso c)

Caso a:
log_4(a) < 2 -> 0 < a < 16

Caso b:
log_4(a) = 2 -> a = 16

Caso c:
log_4(a) > 2 y log_4(a) < log_2(7) -> 16 < a < 49

Conclusión:
La cantidad de subproblemas más grande que puede tomar la solución para que sea mejor que su algoritmo
actual es 48.
"""

"""
.. 3 ..
Se cuenta con un vector de “n” posiciones en el que se encuentran algunos de los primeros ”m” números
naturales ordenados en forma creciente (m >= n). En el vector no hay números repetidos. Se desea obtener
el menor número no incluido.

Ejemplo:
    Array: [1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]
    Solución: 6

    Proponer un algoritmo de tipo división y conquista que resuelva el problema en tiempo inferior a lineal.
    Expresar su relación de recurrencia y calcular su complejidad temporal.
"""

array = [1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]

def find_missing(array):
    return find_missing_aux(array, 0, len(array) - 1)

def find_missing_aux(array, start, end):
    if start == end:
        return start + 1

    middle = (start + end) // 2

    if middle + 1 == array[middle]:
        return find_missing_aux(array, middle + 1, end)
    
    return find_missing_aux(array, start, middle - 1)

# print(find_missing(array))

"""
... 4 ...
Resolver el problema de subarreglo de suma máxima por división y conquista. Calcular la
complejidad del algoritmo. Entrada: Un arreglo A[1..N] de enteros (de cualquier signo)
Salida: Un subarreglo A[i .. j] de A cuya suma es mayor o igual que la de cualquier otro
subarreglo de A.
Ejemplo:
    Array: [-2, -5, 6, -2, -3, 1, 5, -6]
    Solución: [6, -2, -3, 1, 5] 
"""

array = [-2, -5, 6, -2, -3, 1, 5, -6]

def max_sum_until(array, min, max):
    """
    Looking for the best i for a given j
    """
    if min == max:
        return min
    
    middle = (min + max) // 2

    left = max_sum_until(array, min, middle)
    left_sum = sum(array[left:])

    right = max_sum_until(array, middle + 1, max)
    right_sum = sum(array[right:])

    return left if left_sum > right_sum else right

def max_sum(array, min, max):
    """
    Looking for the best j
    """
    if min == max:
        return min
    
    middle = (min + max) // 2

    left = max_sum(array, min, middle)
    left_i = max_sum_until(array[:left], 0, left)
    left_sum = sum(array[left_i:left])

    right = max_sum(array, middle + 1, max)
    right_i = max_sum_until(array[:right], 0, right)
    right_sum = sum(array[right_i:right])

    return left if left_sum > right_sum else right

def max_sum_array(array):
    j = max_sum(array, 0, len(array))
    i = max_sum_until(array, 0, j)
    return array[i:j]

# print(max_sum_array(array))

"""
... Modelo 01 de final ...
... Modelo 04 de final ...
Un grupo de científicos han liberado “n” boyas en diferentes puntos de los océanos para
realizar un estudio sobre las corrientes marinas. Cada boya tiene un emisor de posición
que informa a una computadora central su ubicación cada minuto. Entre los estudios que
desean realizar se encuentra determinar cuales dos boyas se encuentran más cerca entre
sí. Ese proceso lo tienen que realizar en forma eficiente, ya que se realiza de forma
constante y solo es uno de los tantos análisis que realizan. Utilizando división y
conquista proponga una forma de solucionarlo. Explique paso a paso su solución y analice
su complejidad. 
"""

def distancia(boya1, boya2):
    return ((boya1[0] - boya2[0]) ** 2 + (boya1[1] - boya2[1]) ** 2) ** 0.5

def boyas_cercanas(boyas):
    if len(boyas) == 2:
        return boyas
    if len(boyas) == 1:
        return [boyas[0], (float('inf'), float('inf'))]
    if len(boyas) == 0:
        return [(float('inf'), float('inf')), (float('inf'), float('inf'))]
    
    mix_x = min(boyas, key=lambda x: x[0])[0]
    max_x = max(boyas, key=lambda x: x[0])[0]
    mid_x = (mix_x + max_x) / 2
    left_group, right_group = dividir_grupos(boyas, mid_x)
    
    cercanas_izq = boyas_cercanas(left_group)
    cercanas_der = boyas_cercanas(right_group)

    # tengo que ver si hay boyas cercanas entre los dos grupos
    dist_izq = distancia(cercanas_izq[0], cercanas_izq[1]) if len(cercanas_izq) == 2 else float('inf') # O(1)
    dist_der = distancia(cercanas_der[0], cercanas_der[1]) if len(cercanas_der) == 2 else float('inf') # O(1)
    min_dist = min(dist_izq, dist_der) # O(1)
    middle_group = []
    for boya in boyas: # O(n)
        if abs(boya[0] - mid_x) * 2 <= min_dist:
            middle_group.append(boya)

    y_grid_size, grid = armar_grilla_intermedia(mid_x, min_dist, middle_group)
    
    # recorro el grid y veo si hay boyas cercanas
    cercanas = analizar_boyas_intermedias(min_dist, y_grid_size, grid)
    return cercanas

def dividir_grupos(boyas, mid_x):
    left_group = []
    right_group = []
    for boya in boyas: # O(n)
        if boya[0] < mid_x:
            left_group.append(boya)
        else:
            right_group.append(boya)
    return left_group,right_group

def armar_grilla_intermedia(mid_x, min_dist, middle_group):
    min_y = min(middle_group, key=lambda x: x[1])[1]
    max_y = max(middle_group, key=lambda x: x[1])[1]
    y_grid_size = (max_y - min_y) / min_dist
    # grid 4 x y_size
    grid = []
    for i in range(y_grid_size): # O(n)
        grid.append([])
        for j in range(4):
            grid[i].append([])
    for boya in middle_group: # O(n)
        x_index = int((boya[0] - mid_x) / min_dist)
        y_index = int((boya[1] - min_y) / min_dist)
        grid[y_index][x_index].append(boya)
    return y_grid_size,grid

def analizar_boyas_intermedias(min_dist, y_grid_size, grid):
    cercanas = []
    for boya in range(len(grid)): # O(n)
        # hay que ver sólo las 8 celdas vecinas
        x_index = boya[0] # type: ignore
        y_index = boya[1] # type: ignore
        rango_x = range(max(0, x_index - 1), min(4, x_index + 2))
        rango_y = range(max(0, y_index - 1), min(y_grid_size, y_index + 2))
        for i in rango_x: # O(1)
            for j in rango_y:
                for boya2 in grid[i][j]:
                    if boya != boya2:
                        if distancia(boya, boya2) < min_dist:
                            cercanas = [boya, boya2]
                            min_dist = distancia(boya, boya2)
    return cercanas

"""
T(n) = 2T(n/2) + O(n)
a = 2 | b = 2 | c = 1
log_b(a) = c -> T(n) = Θ(n^c log(n)) = Θ(n log(n)) ✅

! -> por deliración mental me acuerdo esto de la clase y me dió bien o cerca de bien, pero messirve 😎
<3 dyc
"""

"""
... Modelo 05 de final ...
Un equipo de trabajo ha realizado una votación anónima para seleccionar a una persona
entre ellos que los represente. En total hay “n” personas. Cada una de ellas realiza
un voto. Tenemos el voto de cada uno de ellos. El líder debe ser seleccionado por más
del 50% del total para ganar. Proponer un algoritmo por división y conquista que
determine si hay un ganador y en caso afirmativo que informe quien es. Analice la
complejidad de su propuesta 
"""

votos = ["A", "B", "A", "C", "B", "A", "C", "C", "B", "C", "A", "A"]

def votacion(votos):
    if len(votos) == 0:
        return 0, None
    
    if len(votos) == 1:
        return 1, votos[0]
    
    middle = len(votos) // 2

    cant1, votado1 = votacion(votos[:middle])
    cant2, votado2 = votacion(votos[middle:])

    if votado1 == votado2:
        return cant1 + cant2, votado1
    
    return (cant1, votado1) if cant1 > cant2 else (cant2, votado2)

# print(votacion(votos))

"""
// Implementar, por división y conquista, una función que dado un arreglo sin elementos repetidos y casi
// ordenado (todos los elementos se encuentran ordenados, salvo uno), obtenga el elemento fuera de lugar.
"""
# en python
def elemento_desordenado(arr):
    if len(arr) == 1:
        return None
    
    middle = len(arr) // 2

    first_half = arr[:middle]
    second_half = arr[middle:]

    if first_half[-1] > second_half[0]:
        return second_half[0]

    op1 = elemento_desordenado(first_half)
    op2 = elemento_desordenado(second_half)

    return op1 if op1 is not None else op2
    

arr = [1, 2, 4, 5, 6, 3, 7, 8, 9]
# print(elemento_desordenado(arr))


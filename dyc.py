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



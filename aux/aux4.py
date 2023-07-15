def merge(array1, array2):
    mergeado = []
    
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            mergeado.append(array1[i])
            i += 1
        else:
            mergeado.append(array2[j])
            j += 1
    
    if i < len(array1):
        mergeado.extend(array1[i:])
    if j < len(array2):
        mergeado.extend(array2[j:])
    return mergeado
     
def _dyc_mergeK_ordenados(arrays, inicio, fin):
    if inicio == fin:
        return arrays[inicio]
        
    medio = (inicio + fin) // 2
    izquierda = _dyc_mergeK_ordenados(arrays, inicio, medio)
    derecha = _dyc_mergeK_ordenados(arrays, medio + 1, fin)
    return merge(izquierda, derecha)

def dyc_mergeK_ordenados(arrays):
    if len(arrays) == 0:
        return []
    return _dyc_mergeK_ordenados(arrays, 0, len(arrays) - 1)

#################################################################

from heapq import heappush, heappop

def heap_mergeK_ordenados(arrays):
    resultado = []
    heap = []

    for i in range(len(arrays)):
        heappush(heap, (arrays[i][0], i, 0))
    
    while heap:
        valor, array_indice, valor_indice = heappop(heap)
        resultado.append(valor)
        if valor_indice + 1 < len(arrays[array_indice]):
            heappush(heap, (arrays[array_indice][valor_indice + 1], array_indice, valor_indice + 1))
        
    return resultado

#################################################################

arrays = [
    [5, 6,  8,  16, 17, 18, 19],
    [3, 7,  12, 13, 20, 21, 22],
    [1, 10, 11, 15, 23, 24, 25],
    [2, 4,  9,  14, 26, 27, 28],
    [5, 6,  8,  16, 17, 18, 19],
    [3, 7,  12, 13, 20, 21, 22],
    [1, 10, 11, 15, 23, 24, 25],
    [2, 4,  9,  14, 26, 27, 28],
    [5, 6,  8,  16, 17, 18, 19],
    [3, 7,  12, 13, 20, 21, 22],
    [1, 10, 11, 15, 23, 24, 25],
    [2, 4,  9,  14, 26, 27, 28],
    [5, 6,  8,  16, 17, 18, 19],
    [3, 7,  12, 13, 20, 21, 22],
    [1, 10, 11, 15, 23, 24, 25],
]

arrays_dyc = dyc_mergeK_ordenados(arrays)
arrays_heap = heap_mergeK_ordenados(arrays)
len_total = 0
for array in arrays:
    len_total += len(array)

for array in arrays:
    for n in array:
        arrays_dyc.remove(n)
        arrays_heap.remove(n)
print(len(arrays_dyc) == 0)
print(len(arrays_heap) == 0)
arrays_heap = heap_mergeK_ordenados([])
arrays_dyc = dyc_mergeK_ordenados([])
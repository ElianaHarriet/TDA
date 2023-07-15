def primer_array(arrays):
    return arrays[0].copy()

def arrayx2(array):
    return [x*2 for x in array]

def arrayx2_inplace(array):
    for i in range(len(array)):
        array[i] *= 2

arrays = [[1,2,3], [4,5,6], [7,8,9]]
print(arrays)
primero = primer_array(arrays)
print(primero)
arrayx2_inplace(primero)
print(primero)
print(arrays)
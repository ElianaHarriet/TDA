# La Escuela Nacional 32 "Alan Turing" de Bragado tiene una forma particular de requerir
# que los alumnos formen fila. En vez del clásico "de menor a mayor altura", lo hacen
# primero con alumnos yendo con altura decreciente, hasta llegado un punto que empieza
# a ir de forma creciente, hasta terminar con todos los alumnos.

# Por ejemplo las alturas podrían ser 1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23.

# Implementar una función indice_mas_bajo que dado un arreglo/lista de alumnos(*) que
# represente dicha fila, devuelva el índice del alumno más bajo, en tiempo logarítmico.
# Se puede asumir que hay al menos 3 alumnos. En el ejemplo, el alumno más bajo es aquel
# con altura 0.98.

# Implementar una función validar_mas_bajo que dado un arreglo/lista de alumnos(*) y un
# índice, valide (devuelva True o False) si dicho índice corresponde al del alumno más
# bajo de la fila.

# (*)
# Los alumnos son de la forma:

# alumno {
#     nombre (string)
#     altura (float)
# }
# Se puede acceder a la altura de un alumno haciendo varible_tipo_alumno.altura.

# Importante: considerar que si la prueba de volumen no pasa, es posible que sea porque
# no están cumpliendo con la complejidad requerida.

# # # # #
# Ejercicio similar en C:
# // Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: estrictamente creciente hasta una
# // determinada posición p, y estrictamente decreciente a partir de ella (con 0 < p < N - 1).

# // Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2.
# // Se pide: implementar un algoritmo de división y conquista de orden O(log(n)) que encuentre la posición
# // p del pico: size_t posicion_pico(int v[], size_t ini, size_t fin);. La función será invocará inicialmente
# // como: posicion_pico(v, 0, n-1), y tiene como pre-condición que el arreglo tenga forma de pico.
# size_t posicion_pico(int v[], size_t desde, size_t hasta) {
#     if (desde == hasta) {
#         return desde;
#     }
#     size_t medio = (desde + hasta) / 2;
#     if (v[medio - 1] < v[medio] && v[medio] > v[medio + 1]) {
#         return medio;
#     } else if (v[medio - 1] < v[medio]) {
#         return posicion_pico(v, medio, hasta);
#     } else {
#         return posicion_pico(v, desde, medio);
#     }
# }
# # # # #

# # # # #
class alumno:
    def __init__(self, nombre, altura):
        self.nombre = nombre # string
        self.altura = altura # float
# # # # #

def _indice_mas_bajo(alumnos, desde, hasta):
    # Complejidad esperada: O(log(n))
    # Pre-condición: hay al menos 3 alumnos.
    if desde == hasta:
        return desde
    
    medio = (desde + hasta) // 2
    alumno_pre_medio = alumnos[medio - 1]
    alumno_medio = alumnos[medio]
    alumno_post_medio = alumnos[medio + 1]

    if alumno_pre_medio.altura > alumno_medio.altura and alumno_medio.altura < alumno_post_medio.altura:
        return medio
    elif alumno_pre_medio.altura > alumno_medio.altura:
        return _indice_mas_bajo(alumnos, medio + 1, hasta)
    else:
        return _indice_mas_bajo(alumnos, desde, medio - 1)

def indice_mas_bajo(alumnos):
    # Devuelve el índice del alumno más bajo de la fila.
    # Complejidad esperada: O(log(n))
    # Pre-condición: hay al menos 3 alumnos.
    return _indice_mas_bajo(alumnos, 0, len(alumnos) - 1)

def validar_mas_bajo(alumnos, indice):
    # Valida que el índice corresponda al del alumno más bajo de la fila.
    # Complejidad esperada: O(1)
    # Pre-condición: hay al menos 3 alumnos.
    alumno_pre_indice = alumnos[indice - 1] if 0 <= indice - 1 else None
    alumno_indice = alumnos[indice]
    alumno_post_indice = alumnos[indice + 1] if indice + 1 < len(alumnos) else None
    
    cond_a = alumno_pre_indice is None or alumno_pre_indice.altura > alumno_indice.altura
    cond_b = alumno_post_indice is None or alumno_post_indice.altura > alumno_indice.altura
    return cond_a and cond_b

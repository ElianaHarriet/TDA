.. 1 ..
Nos dan una caja negra A que, dado un grafo no dirigido G = (V, E) y un número k
se comporta de la siguiente manera:
Si G es no conexo devuelve “no conexo”.
Si G es conexo y tiene un conjunto independiente de tamaño al menos k devuelve “Sí”.
Si G es conexo y no tiene un conjunto independiente de tamaño al menos k devuelve “No”.

Mostrar cómo podríamos resolver el problema del máximo conjunto independiente en tiempo
polinomial, usando llamadas a A si suponemos que A corre en tiempo polinomial en el
tamaño de G y k. Describir la solución. ¿Tiene sentido la hipótesis de que A corre en
tiempo polinomial en el tamaño de G y k? ¿Por qué? 


Para resolver el problema del máximo conjunto independiente en tiempo polinomial, usamos
el algoritmo de búsqueda binaria.
1. Se obtiene la cantidad V de vértices del grafo G, ese valor es el límite superior del
   conjunto independiente. Por lo tanto k comienza en V/2, el mínimo es 0 y el máximo es V.
2. Si el mínimo es igual al máximo, entonces el conjunto independiente es de tamaño k.
3. Se llama a la caja negra A con el grafo G y el valor de k.
   a. Si A devuelve "Sí", entonces el máximo conjunto independiente es de al menos k, por lo
      tanto el nuevo mínimo es k y el máximo se mantiene, k = (mínimo + k)//2. Se vuelve al
      paso 2.
   b. Si A devuelve "No", entonces el máximo conjunto independiente es de menos de k, por lo
      tanto el nuevo máximo es k, el mínimo se mantiene y k = (mínimo + k)//2. Se vuelve al
      paso 2.
   c. Si A devuelve "no conexo", entonces el grafo no es conexo, por lo tanto no tiene un
      conjunto independiente. Se devuelve "No".

El orden del algoritmo es O( log(V) * O(A) ), lo cual si O(A) es polinomial, entonces el
algoritmo es polinomial.
Como encontrar el máximo conjunto independiente es NP-Completo, entonces O( log(V) * O(A) )
no puede ser polinomial. Y, de esta forma, no tiene sentido la hipótesis de que A corre en
tiempo polinomial en el tamaño de G y k.

##############################################################################################

.. 3 ..
Un almacén registra en una matriz qué productos compra cada uno de sus clientes. Un conjunto
de clientes es diverso si cada uno de ellos compra cosas diferentes (tiene intersección vacía
con lo que compran los demás). Problema de los clientes diversos: Dada una matriz de registro,
de tamaño m (clientes) x n (productos), y un número k<=m, ¿existe un subconjunto de tamaño al
menos k de los clientes que sea diverso?

Probar que el Problema de los clientes diversos es NP-completo.
(Pista: Reducir polinomialmente conjuntos independientes a clientes diversos)

Ejemplo de matriz de registro:
        Vino        Fideos      Tomates     Queso
Ana     1           3                       3
Juan                            4
Pedro   2                       1           1


Para demostrar que el problema de los clientes diversos es NP-Completo, reducimos el problema
de independent set a este problema.

Tenemos un grafo para buscar el independent set, lo vamos a representar con una matriz de
incidencias.

A   B   C   D   E   F
1   1   0   0   0   0
1   0   1   0   0   0
0   1   0   1   0   0
0   1   0   0   1   0
0   0   1   0   1   0
0   0   1   0   0   1
0   0   0   1   1   0
0   0   0   0   1   1

Ahora ese grafo, tenemos que llevarlo a una matriz de registro, donde las filas representan
a los clientes y las columnas a los productos. Que dos vértices estén conectados, significa
que ambos compran el mismo producto. Por lo tanto, vamos a transponer la matriz de
incidencias y nombrar cada arista con el nombre de un producto.
    
    P1  P2  P3  P4  P5  P6  P7  P8
A   1   1   0   0   0   0   0   0
B   1   0   1   1   0   0   0   0
C   0   1   0   0   1   1   0   0
D   0   0   1   0   0   0   1   0
E   0   0   0   1   1   0   1   1
F   0   0   0   0   0   1   0   1

Para este ejemplo, vamos a suponer que k = 3. Y vamos a pedirle al algoritmo de los clientes
que nos devuelva un conjunto de clientes de tamaño 3 que sea diverso.
Lo cual nos va a devolver el conjunto {A, D, F} ya que A compra P1 y P2, D compra P3 y P7 y
F compra P6 y P8. Por lo tanto, el conjunto es diverso.

##############################################################################################

... 4 ...
La siguiente es una versión de Independet Set. Dado un grafo G= (V, E) y un entero k, decimos
que I ⊆ V es fuertemente independiente si dados dos vértices u y v en I, la arista (v, u) no
pertenece a E y además no hay ningún camino de tamaño 2 (con dos aristas) de u a v.
El problema de Strongly Independent Sets consiste en decidir si G tiene un conjunto fuertemente
independiente de tamaño al menos k. Probar que el problema de Strongly Independent Sets es NP
completo (y para eso usar que Independent Set es NP completo).

-> miro

##############################################################################################

... Modelo 01 de final ...
Se requiere realizar un viaje a través de un territorio de difícil acceso. El mismo se
encuentra dividido en zonas por las que se debe pasar. Existen m facciones que controlan
algunas de esas zonas. Una facción puede controlar más de 1 zona y una zona puede ser
controlada por más de una. Para poder realizar el viaje se debe pactar con alguna de
estas. Cada pacto con una facción nos asegura el paso seguro por todas las zonas que
controlan independientemente de si alguna de sus zonas son también controladas por otras
facciones. Deseamos saber si es posible pactar con no más de k facciones para poder
concretar el viaje de forma segura.
Se pide: Demostrar que el problema es NP-Completo.
HINT: Se puede utilizar Vertex Cover.

-> miro

##############################################################################################


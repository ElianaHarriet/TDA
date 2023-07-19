"""
... Modelo 03 de final ...
Una empresa multinacional está revisando su lista de proveedores. Tienen una lista de “n” productos,
materias primas e insumos que adquieren todos los meses. Su proceso de compras es muy descentralizado
y tienen un número actual de “m” proveedores. Piensan que pueden bajar los costos si reducen la
cantidad de proveedores. Saben qué productos ofrece cada proveedor. Las diferencias de precios son
despreciables, lo que quieren es encontrar el conjunto menor posible de proveedores para cubrir toda su
necesidades de productos.
Proponer un algoritmo eficiente que aproxime la solución óptima. Explique su funcionamiento. Detalle
complejidad temporal y que tan diferente a la solución óptima puede lograr con su método. 
"""

# Se pide una aproximación a vertex cover

# dict_proveedores: proveedor -> productos
def filtrar_proveedores(lista_productos, dict_proveedores): # O(n + m) -> ya que recorre todos los productos y proveedores
    proveedores_filtrados = {}
    for proveedor, productos in dict_proveedores.items():
        for producto in productos:
            if producto in lista_productos:
                proveedores_filtrados[proveedor] = proveedores_filtrados.get(proveedor, set()) | {producto}
    return proveedores_filtrados

def mas_importante(dict_proveedores): # O(n + m) -> ya que recorre todos los productos y proveedores
    proveedor_mas_importante = None
    productos_mas_importante = set()
    for proveedor, productos in dict_proveedores.items():
        if len(productos) > len(productos_mas_importante):
            proveedor_mas_importante = proveedor
            productos_mas_importante = productos
    return proveedor_mas_importante

def elegir_proveedores(lista_productos, dict_proveedores): # O(n * (n + m)) -> O(n^2 + n * m)
    proveedores = set()
    
    productos_restantes = set(lista_productos)
    proveedores_filtrados = filtrar_proveedores(lista_productos, dict_proveedores)
    while len(productos_restantes) > 0: # Como mucho se recorre n veces
        proveedor = mas_importante(proveedores_filtrados) # O(n + m)
        proveedores.add(proveedor)
        productos_restantes -= proveedores_filtrados[proveedor]
        del proveedores_filtrados[proveedor]
        proveedores_filtrados = filtrar_proveedores(productos_restantes, proveedores_filtrados) # O(n + m)
    return proveedores

lista_productos = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
dict_proveedores = {
        "P1": ["A", "B", "C", "D", "E"],
        "P2": ["A", "B", "C", "D", "E", "F", "G"],
        "P3": ["E", "F", "G", "H", "I"],
        "P4": ["J", "K", "L", "M", "N", "O", "P", "Q", "R"],
        "P5": ["A", "B", "C", "D", "H", "J", "K", "L", "M", "N", "O", "P", "Q", "R"],
    }
# print(elegir_proveedores(lista_productos, dict_proveedores))

# TODO -> calcular tipo de aproximación

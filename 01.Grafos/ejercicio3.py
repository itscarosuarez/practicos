import json

def cargar_grafo(archivo):
    f = open(archivo)
    estructura = json.load(f)
    f.close()
    return estructura

def busqueda_paso(estructura, s, t):
    OPEN = [(s, None)]
    CLOSED = []
    
    while OPEN:
        z, y = OPEN.pop(0)
        CLOSED.append((z, y))
        
        if z == t:
            return reconstruir_paso(CLOSED, s, t)
        
        if z in estructura['E']:
            for w in estructura['E'][z]:
                if not esta_en_closed(w, CLOSED) and not esta_en_open(w, OPEN):
                    OPEN.append((w, z))
    
    return None

def esta_en_closed(nodo, CLOSED):
    for z, y in CLOSED:
        if z == nodo:
            return True
    return False

def esta_en_open(nodo, OPEN):
    for z, y in OPEN:
        if z == nodo:
            return True
    return False

def reconstruir_paso(CLOSED, s, t):
    paso = []
    nodo_actual = t
    
    while nodo_actual != s:
        paso.append(nodo_actual)
        for z, y in CLOSED:
            if z == nodo_actual:
                nodo_actual = y
                break
    
    paso.append(s)
    paso.reverse()
    return paso

estructura = cargar_grafo('esDivisorDe-200.json')

print("Ejemplo 1: Paso de 2 a 16")
paso = busqueda_paso(estructura, '2', '16')
if paso:
    print("Paso encontrado:", " -> ".join(paso))
else:
    print("No existe paso")

print("\nEjemplo 2: Paso de 3 a 18")
paso = busqueda_paso(estructura, '3', '18')
if paso:
    print("Paso encontrado:", " -> ".join(paso))
else:
    print("No existe paso")

print("\nEjemplo 3: Paso de 5 a 100")
paso = busqueda_paso(estructura, '5', '100')
if paso:
    print("Paso encontrado:", " -> ".join(paso))
else:
    print("No existe paso")

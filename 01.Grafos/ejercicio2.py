import json

def esReflex(verts, aristas):
    for v in verts:
        if v not in aristas[v]:
            return False
    return True

def esSim(verts, aristas):
    for v in verts:
        for vecino in aristas[v]:
            if v not in aristas.get(vecino, []):
                return False
    return True

def esAntisim(verts, aristas):
    for v in verts:
        for vecino in aristas[v]:
            if v != vecino and vecino in aristas[v] and v in aristas.get(vecino, []):
                return False
    return True

def esTrans(verts, aristas):
    for v in verts:
        for vecino in aristas[v]:
            for tercero in aristas.get(vecino, []):
                if tercero not in aristas[v]:
                    return False
    return True

def analizar(arch):
    with open(arch, 'r') as f:
        data = json.load(f)
    
    verts = data['P']
    aristas = data['E']
    
    es_refl = esReflex(verts, aristas)
    es_sim = esSim(verts, aristas)
    es_antisim = esAntisim(verts, aristas)
    es_trans = esTrans(verts, aristas)
    
    print(f"Archivo: {arch}")
    print(f"Reflexividad: {'Si' if es_refl else 'No'}")
    print(f"Simetria: {'Si' if es_sim else 'No'}")
    print(f"Antisimetria: {'Si' if es_antisim else 'No'}")
    print(f"Transitividad: {'Si' if es_trans else 'No'}")
    
    if es_refl and es_antisim and es_trans:
        print("Tipo: Orden parcial")
    elif es_refl and es_sim and es_trans:
        print("Tipo: Relación de equivalencia")
    else:
        print("Tipo: Ninguno")
    print()

archivos = ["01.json", "02.json", "03.json"]
for arch in archivos:
    try:
        analizar(arch)
    except:
        print(f"Error procesando {arch}")
print()

import json
import hito_3


def graph():    
    calles = []
    coordenadas = []
    calles=hito_3.leerCalles()
    I = hito_3.generarIntersecciones(calles, "source/Intersecciones con coordenadas.txt", 42, 44, coordenadas)
    hito_3.generarListaAdyacencia(I, coordenadas, 9)
    #Loc = [(10, 10), (10, 24), (23, 22), (22, 11)]
    G = []
    with open("source/Lista_Adyacencia_Generado.txt") as f:
        for line in f:
            nums = [float(x) for x in line.split()]
            G.append([])
            for i in range(0, len(nums), 2):
                G[-1].append((int(nums[i]), nums[i+1]))
    
    response = {"loc": coordenadas, "g": G}

    return json.dumps(response)

def paths():
    calles = []
    coordenadas = []
    calles=hito_3.leerCalles()
    I = hito_3.generarIntersecciones(calles, "source/Intersecciones con coordenadas.txt", 42, 44, coordenadas)
    hito_3.generarListaAdyacencia(I, coordenadas, 9)
    #Loc = [(10, 10), (10, 24), (23, 22), (22, 11)]
    G = []
    with open("source/Lista_Adyacencia_Generado.txt") as f:
        for line in f:
            nums = [float(x) for x in line.split()]
            G.append([])
            for i in range(0, len(nums), 2):
                G[-1].append((int(nums[i]), nums[i+1]))
    op1 = 1
    op2 = 38

    if (op1 >= 0 and op1 <= 1728) and (op2 >= 0 and op2 <= 1728):
        shortest_paths = []
        p = 0
        for _ in range(3):
            n_path, p = hito_3.function_path(G, op1, op2, p)
            shortest_paths.append(n_path)
    
        bestpath = shortest_paths[0]
        path1 = shortest_paths[1]
        path2 = shortest_paths[2]

    response = {"bestpath": bestpath, "path1": path1, "path2": path2}

    return json.dumps(response)


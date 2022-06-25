import numpy as np
import random
import math
import heapq as hq


def leerCalles():
  calles = []
  with open("source/Calles.txt") as f:
      for line in f:
        calle = line.split()
        calles.append(*calle)
  return calles

def generarIntersecciones(calles, archivo, nfilas, ncol, coordenadas):
  n = len(calles)
  if n == nfilas + ncol:
    num = 0
    dicc_c = {}
    for calle in calles:
      dicc_c[calle] = num
      num += 1
    
    I = np.zeros([nfilas,ncol], int)
    I = I - 1

    with open(archivo) as f:
      for line in f:
        nodo, fila, columna, latitud, longitud = [elem for elem in line.split()]
        I[dicc_c[fila], dicc_c[columna] - nfilas] = int(nodo)
        coordenadas.append((float(latitud), float(longitud)))

  return I


class Perlin:
    def __init__(self):
        self.gradients = []
        self.lowerBound = 0


    def valueAt(self, t,max):
        if(t<self.lowerBound):
            print("ERROR: Input parameter out of bounds!")
            return
        while t >= len(self.gradients)-1+self.lowerBound:
            self.gradients.append(random.uniform(1, max))

        discarded = int(self.lowerBound) # getting number of gradients that have been discarded
        # Compute products between surrounding gradients and distances from them
        d1 = (t-t//1)
        d2 = d1-1
        a1 = self.gradients[(int)(t//1)-discarded]*d1
        a2 = self.gradients[(int)(t//1+1)-discarded]*d2

        amt = self.__ease(d1)

        return self.__lerp(a1,a2,amt)

    def discard(self, amount):
        gradientsToDiscard = int(amount+self.lowerBound%1)
        self.gradients = self.gradients[gradientsToDiscard:]
        self.lowerBound += amount

    def __ease(self, x):
        return 6*x**5-15*x**4+10*x**3


    def __lerp(self, start, stop, amt):
        return amt*(stop-start)+start


def updateTraffic(hour):
  noise=Perlin()
  time=[i*0.01 for i in range(1729)]
  if hour>22 or hour<4:
    values=[int(abs(noise.valueAt(i,20)*2)) for i in time]
    return values
  if hour>=4 and hour<10:
    values=[int(abs(noise.valueAt(i,50)*10)) for i in time]
    return values
  if hour>=10 and hour<14:
    values=[int(abs(noise.valueAt(i,35)*8)) for i in time]
    return values
  if hour>=14 and hour<22:
    values=[int(abs(noise.valueAt(i,45)*10)) for i in time]
    return values

def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia

def peso2calculo(trafficValue):
  a=50-trafficValue
  if a>=25:
    peso2=1.3
    return peso2
  else:
    peso2=0.7
    return peso2


def generarListaAdyacencia(I, coordenadas, hora):
  G = []
  nfilas, ncol = np.shape(I) 
  values=updateTraffic(hora)
  #Agregar las adyacencias de cada nodo
  for i in range(nfilas):
    for j in range(ncol):
      if I[i,j] > -1:
        aux = []
        latitud1, longitud1 = coordenadas[I[i,j]]
        #arriba
        if (i > 0) and (I[i-1, j] > -1):
          latitud2, longitud2 = coordenadas[I[i-1, j]]
          peso1 = haversine(latitud1, longitud1, latitud2, longitud2)
          traficcValue=values[i+1]
          peso2=peso2calculo(traficcValue)
          peso=peso1*peso2
          aux.append(I[i-1, j])
          aux.append(peso)
        #izquierda
        if (j > 0) and (I[i, j-1] > -1):
          latitud2, longitud2 = coordenadas[I[i, j-1]]
          peso1 = haversine(latitud1, longitud1, latitud2, longitud2)
          traficcValue=values[i+1]
          peso2=peso2calculo(traficcValue)
          peso=peso1*peso2
          aux.append(I[i, j-1])
          aux.append(peso)
        #derecha
        if (j < ncol-1) and (I[i, j+1] > -1):
          latitud2, longitud2 = coordenadas[I[i, j+1]]
          peso1 = haversine(latitud1, longitud1, latitud2, longitud2)
          traficcValue=values[i+1]
          peso2=peso2calculo(traficcValue)
          peso=peso1*peso2
          aux.append(I[i, j+1])
          aux.append(peso)
        #abajo
        if (i < nfilas-1) and (I[i+1, j] > -1):
          latitud2, longitud2 = coordenadas[I[i+1, j]]
          peso1 = haversine(latitud1, longitud1, latitud2, longitud2)
          traficcValue=values[i+1]
          peso2=peso2calculo(traficcValue)
          peso=peso1*peso2
          aux.append(I[i+1, j])
          aux.append(peso)
        G.append(aux)

  #Guardar en un archivo
  with open("source/Lista_Adyacencia_Generado.txt", 'w') as archivo:
    for lista in G:
      for num in lista:
        archivo.write(str(num) + " ")
      archivo.write("\n")

def dijkstra(G, s, e, p):
  n = len(G)
  visited = [False]*n
  path = [-1]*n
  cost = [math.inf]*n

  cost[s] = 0
  pqueue = [(0, s)]
  while pqueue:
    g, u = hq.heappop(pqueue)
    if u == e:
      break
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        if not visited[v]:
          f = g + w
          if f < cost[v]:
            if (v == e) and (f <= p):
              pass
            else:
              cost[v] = f
              path[v] = u
              hq.heappush(pqueue, (f, v))
            
  return path, cost

def path_visualization(path, end):
  n = len(path)
  new_path = [-1]*n
  while path[end] > -1:
    new_path[end] = path[end]
    end = path[end]
  return new_path

def function_path(G, first, end, p):
  path, cost =dijkstra(G, first, end, p)
  p = cost[end]
  if p == math.inf:
    return
  else:
    n_path = path_visualization(path, end)
    return n_path, p



import sys
import heapq
#import time

def main(N,M,P,p,e):
    
    portales = p
    energias = e

    
    grafo = {}
    
    # se definen los arcos de los movimientos horizontales
    for j in range(1,M):
        for i in range(1,N+1):
            if (i,j) not in grafo:            
                grafo[(i,j)] = {(i,j+1) : energias[i-1]}
            else:
                grafo[(i,j)][(i,j+1)] = energias[i-1]
            
            if (i,j+1) not in grafo:            
                grafo[(i,j+1)] = {(i,j) : energias[i-1]}
            else:
                grafo[(i,j+1)][(i,j)] = energias[i-1]
            
    
    # se definen los arcos de los portales, la energia es 0 
    for portal in portales:
        x1, y1, x2, y2 = portal
        
        if (x1,y1) not in grafo:            
            grafo[(x1,y1)] = {(x2,y2) : 0}
        else:
            grafo[(x1,y1)][(x2,y2)] = 0
    
    
    try :
        distancias = calcular_distancias(grafo, (1,1))
        distancia_objetivo = distancias.get((N,M))
        
        if distancia_objetivo == float("inf"):
            print("NO EXISTE")
        else:
            print(distancia_objetivo)
            
    except Exception:
        # solo ocurre cuando solo hay un cuarto por piso
        print('NO EXISTE') 
        
         
        
        
def calcular_distancias(grafo, vertice_inicial):
    
    distancias = {vertice: float('infinity') for vertice in grafo}
    distancias[vertice_inicial] = 0


    pq = [(0, vertice_inicial)]
    while len(pq) > 0:
        distancia_actual, vertice_actual = heapq.heappop(pq)

        # Los vertices se pueden aniadir a la cola de prioridad varias veces
        # Solo se procesa un vergtice la primera vez que se elimina de la pq
        
        if distancia_actual > distancias[vertice_actual]:
            continue

        for vecino, peso in grafo[vertice_actual].items():
            distancia = distancia_actual + peso

            # Solo considera el nuevo comino si es mejor a cualquier otro camino consider this new path if it's better than any path we've
            # encontrado anteriormente 
            
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(pq, (distancia, vecino))

    return distancias
        
    
#inicial = time.time()
numero_casos = int(sys.stdin.readline())
for num in range(numero_casos):
    sizes = list(map(int, sys.stdin.readline().split()))
    N = sizes[0]
    M = sizes[1]
    P = sizes[2]
    e = list(map(int, sys.stdin.readline().split()))
    p = [0]*P
    
    
    for i in range(P):
        p[i] = (list(map(int, sys.stdin.readline().split())))

    main(N,M,P,p,e)

#final = time.time()
#print(final-inicial)

import heapq


def main():
      
    N = 31
    M = 1
    P = 24
    portales = [[1, 1, 5, 1], [2, 1, 4, 1], [3, 1, 13, 1], [4, 1, 27, 1], [5, 1, 26, 1], [6, 1, 15, 1], [7, 1, 9, 1], [10, 1, 25, 1], [11, 1, 13, 1], [12, 1, 21, 1], [9, 1, 12, 1], [14, 1, 19, 1], [16, 1, 31, 1], [17, 1, 19, 1], [18, 1, 30, 1], [20, 1, 21, 1], [19, 1, 21, 1], [22, 1, 25, 1], [23, 1, 29, 1], [24, 1, 29, 1], [25, 1, 31, 1], [15, 1, 25, 1], [27, 1, 29, 1], [28, 1, 31, 1]]
    energias = [348, 295, 984, 334, 393, 571, 868, 257, 462, 834, 635, 490, 240, 335, 533, 220, 688, 284, 683, 973, 516, 296, 650, 805, 666, 155, 342, 139, 999, 836, 636]

    # se definen los vertices como parejas (i,j) donde i es el piso (fila) y j es el cuarto (columna)
    vertices = [(i,j) for i in range(1,N+1) for j in range(1,M+1)]
    
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
        distancias = calculate_distances(grafo, (1,1))
        distancia_objetivo = distancias.get((N,M))
        
        if distancia_objetivo == float("inf"):
            print("NO EXISTE")
        else:
            print(distancia_objetivo)
            
    except Exception:   
        print('NO EXISTE') 
        
       
            
         
        
        
def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
        

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
    

if __name__ == '__main__':
    main()
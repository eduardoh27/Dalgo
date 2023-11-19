from queue import PriorityQueue # essentially a binary heap


def main():
    
    N=4 # pisos
    M=3 # cuartos
    P=4 # portales
    portales = [[1, 2, 3, 1], [1, 3, 4, 3], [2, 1, 4, 2], [3, 2, 4, 1]]
    energias = [2, 1, 3, 0]
   
    """
    
    N=5
    M=3
    P=3
    energias = [5,17,8,1,4]
    portales = [[1, 3 ,3 ,3],
[3, 1 ,5 ,2],
[3, 2, 5 ,1]
]
    """
 
    N=6
    M=3
    P=3
    energias = [5,17,8,1,4,2]
    portales = [[1, 3 ,3 ,3],
    [3, 1 ,5 ,2],
    [3, 2, 5 ,1]
    ]
    
    N=5
    M=3
    P=1
    energias = [5,17,8,1,4]
    portales = [[1, 3 ,5,3]
    ]
 
    
    N=5
    M=5
    P=5
    energias = [3,2,3,7,5]
    portales = [[3,5,4,2],
                [2,2,5,4],
                [4,4,5,2],
                [1,2,4,2],
                [3,3,5,2]
    ]
    
    
    # se definen los vertices como parejas (i,j) donde i es el piso (fila) y j es el cuarto (columna)
    vertices = [(i,j) for i in range(1,N+1) for j in range(1,M+1)]
    
    # se definen los arcos de los movimientos horizontales a la derecha
    arcos = {((i,j),(i,j+1)): energias[i-1] for i in range(1,N+1) for j in range(1,M)}
    
    # se definen los arcos de los movimientos horizontales a la izquierda
    for j in range(1,M):
        for i in range(1,N+1):            
            arcos[((i,j+1),(i,j))] = energias[i-1]  
    
    # se definen los arcos de los portales, la energia es 0 
    for portal in portales:
        x1, y1, x2, y2 = portal
        arcos[(x1,y1),(x2,y2)] = 0

    distancias = dijkstra(vertices, arcos)
    print(distancias)
    
    
def dijkstra(g, start, goal):
    """ Uniform-cost search / dijkstra """
    visited = set()
    cost = {start: 0}
    parent = {start: None}
    todo = PriorityQueue()
  
    todo.put((0, start))
    while todo:
        while not todo.empty():
            _, vertex = todo.get() # finds lowest cost vertex
            # loop until we get a fresh vertex
            if vertex not in visited: break
        else: # if todo ran out
            break # quit main loop
        visited.add(vertex)
        if vertex == goal:
            break
        for neighbor, distance in G[vertex]:
            if neighbor in visited: continue # skip these to save time
            old_cost = cost.get(neighbor, float('inf')) # default to infinity
            new_cost = cost[vertex] + distance
            if new_cost < old_cost:
                todo.put((new_cost, neighbor))
                cost[neighbor] = new_cost
                parent[neighbor] = vertex

    return parent

def make_path(parent, goal):
    if goal not in parent:
        return None
    v = goal
    path = []
    while v is not None: # root has null parent
        path.append(v)
        v = parent[v]
    return path[::-1]

if __name__ == '__main__':
    main()
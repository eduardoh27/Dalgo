

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
    
def dijkstra(nodes,edges,source_index=(1,1)):
    
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[source_index] = 0
    
    adjacent_nodes = {v: {} for v in nodes}
    for (u, v), w_uv in edges.items():
        adjacent_nodes[u][v] = w_uv 
        
    temporary_nodes = [v for v in nodes]
    while len(temporary_nodes) > 0:
        upper_bonds = {v: path_lengths[v] for v in temporary_nodes}
        u = min(upper_bonds, key=upper_bonds.get)
        
        temporary_nodes.remove(u)
        for v, w_uv in adjacent_nodes[u].items():
            if v in temporary_nodes:
                path_lengths[v] = min(path_lengths[v], path_lengths[u] + w_uv) 
            
    return path_lengths
        
    

if __name__ == '__main__':
    main()
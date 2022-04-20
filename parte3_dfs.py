
import sys
    

def dfs(vertices, edges):
    
    colores = ["WHITE"] * len(vertices)
    pis = ["NIL"] * len(vertices)
    inicios = [None] * len(vertices)
    fines = [None] * len(vertices)
    
    cycle = False
    time = 0
    
    for u in vertices:
        if colores[u] == "WHITE":
            time, colores, pis, inicios, fines, cycle = dfs_visit(vertices, edges, u, time, colores, pis, inicios, fines, cycle)

    
    if cycle:
        print("Existe al menos un ciclo en el grafo.")
    else:
        orden_topologico(fines)
        
def orden_topologico(fines):
    
    dic = {}
    for i in range(len(fines)):
        dic[fines[i]] = i
    
    sor = sorted(dic, reverse= True )     
    top_order = []
    for j in sor:
        top_order.append(dic[j])

    print(f'Un orden topológico para el grafo es: {top_order}.')
        
    
def dfs_visit(vertices, edges, u, time, colores, pis, inicios, fines, cycle):
 
    time += 1
    inicios[u] = time
    colores[u] = "GRAY"
    
    for v in edges[u]:
        if colores[v] == "GRAY":
            cycle = True	
        elif colores[v] == "WHITE":
            pis[v] = u
            time, colores, pis, inicios, fines, cycle = dfs_visit(vertices, edges, v, time, colores, pis, inicios, fines, cycle)
    
    colores[u] = "BLACK"        
    time += 1
    fines[u] = time
    
    return time, colores, pis, inicios, fines, cycle
    
  
  
def main():
    
    fila1 = list(map(int, sys.stdin.readline().split()))
    size = len(fila1)

    vertices = [i for i in range(size)]
    edges = [[] for i in range(size)]
    
    pos = 0
    for j in fila1:
        if j > 1:
            edges[0].append(pos)
        pos+=1            
            
    for num in range(1,size):    
        
        fila = list(map(int, sys.stdin.readline().split()))
        
        pos = 0
        for j in fila:
            if j > 0:
                edges[num].append(pos)
            pos+=1  
    
    #vertices = [0,1,2,3,4,5,6,7]
    #edges = [[4],[0,5] ,[], [2,7], [], [0,2], [2,3,5,7], []]

    dfs(vertices, edges)
    

    
if __name__ == "__main__":
         
    main()
    
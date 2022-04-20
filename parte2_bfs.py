
import sys


def componentes_conectados(grafo):
    
    comps = []
    
    visitados = set()
    
    componente = set()
    
    for vertice in grafo:
        if vertice not in visitados:
            comps.append(componente)
            componente = set()
            bfs(grafo, vertice, visitados, componente)
            
    comps.append(componente)
    comps.pop(0)
    
    print(comps)


def bfs(grafo, vertice, visitados, componente):

    cola = [vertice]
    while len(cola) > 0:
        vertice = cola.pop(0)
        if vertice not in visitados:
            visitados.add(vertice)
            componente.add(vertice)
            faltantes = grafo[vertice] - visitados
            cola.extend(faltantes)

  
def main():
    
    fila1 = list(map(int, sys.stdin.readline().split()))
    size = len(fila1)

    grafo = {}
    
    grafo[0]=set()
    pos = 0
    for j in fila1:
        if j == 1:
            grafo[0].add(pos)
        pos+=1            
            
    for num in range(1,size):    
        
        fila = list(map(int, sys.stdin.readline().split()))
        
        grafo[num]=set()
        pos = 0
        for j in fila:
            if j == 1:
                grafo[num].add(pos)
            pos+=1  
    
    componentes_conectados(grafo)

    
if __name__ == "__main__":
         
    main()
    
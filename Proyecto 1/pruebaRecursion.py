import sys
import heapq
import time
import traceback


def findMin(i,j, N, M, energias, portales, matriz_distancias):
    print(i,j)
    if i == (N-1) and j == (M-1):
        return 0
    
    
    elif i == (N-1):
        print(i, N-1)
        print("a", N-1)
        return ((M-1) - (j)) * energias[i]
    
    elif i < (N-1):
        portales_gasto = [] # portales en el mismo piso que llevan al ultimo piso o algun piso superior:
        for portal in portales:
            x1, y1, x2, y2 = portal
            if (x1-1) == i:
                dif_cuartos = abs(y2-y1) 
                gasto_horizontal_portal = dif_cuartos * energias[i]
                gasto_destino_portal = findMin(x2-1, y2-1, N, M, energias, portales, matriz_distancias)
                gasto_portal = gasto_horizontal_portal + gasto_destino_portal
                portales_gasto.append(gasto_portal)
                
        
        if len(portales_gasto) == 0:
            return "else"
        else:   
            min(portales_gasto)
    
    else:
        return "else"
            
            
        
        


def main():


    N = 4
    M = 3
    P = 4
    portales = [[1, 2, 3, 1], 
                [1, 3, 4, 3], 
                [2, 1, 4, 2], 
                [3, 2, 4, 1]]
    energias = [2,1,3,0]


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
    
    matriz_distancias = [[0]*M for i in range(N)] #[N][M]
    
    for i in reversed(range(N)): # va fila por fila cambiando cuartos
        for j in reversed(range(M)):
            
            print(f'\n{matriz_distancias}')
            print(i,j)
            matriz_distancias[i][j] = findMin(i,j, N, M, energias, portales, matriz_distancias)




           
if __name__ == '__main__':
    main()
    
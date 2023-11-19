import sys


class Graph:
    def __init__(self, N, M):
        self.V = N*M
        self.N = N
        self.M = M
        self.graph = [[-1 for j in range(self.V)] for i in range(self.V)]

    def printSolution(self, dist):
        print("Vertex \t Distance from source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def minDistance(self, dist, sptSet):

        min = sys.maxsize  # infinity
        min_index = -1

        for u in range(self.V):
            if dist[u] <= min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    def dijkstra(self, source):
        distance = [sys.maxsize] * self.V
        sptSet = [False] * self.V
        distance[source] = 0

        for i in range(self.V):
            u = self.minDistance(distance, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] >= 0 and (not sptSet[v]) and distance[u] + self.graph[u][v] < distance[v]:
                    distance[v] = distance[u] + self.graph[u][v]
        self.printSolution(distance)


def make_matrix_adj(p, e, P, N, M, G:Graph):
    # aquí se confía que las coordenadas del portal cumplen 0<=x<N y 0<=y<M
    i = 0
    for j in range(1, N*M):
        if j % M == 0:
            i = i+1
            continue
            print(j)
        G.graph[j - 1][j] = e[i]
        G.graph[j][j - 1] = e[i]
        print("vertices: " +str(j)+","+str(j-1))
    for i in range(P):
        u = (p[i][0]-1)*M + (p[i][1]-1)
        v = (p[i][2]-1)*M + (p[i][3]-1)
        print("vertices: " + str(u) + "," + str(v))
        G.graph[u][v] = 0

    for k in range(N*M):
        print("adj matrix:"+ str(G.graph[k]))



numero_casos = int(sys.stdin.readline())
for __ in range(numero_casos):
    sizes = list(map(int, sys.stdin.readline().split()))
    N = sizes[0]
    M = sizes[1]
    P = sizes[2]
    e = list(map(int, sys.stdin.readline().split()))
    p = [0]*P
    for i in range(P):
        p[i] = (list(map(int, sys.stdin.readline().split())))
    print("N:" + str(N))
    print("M:" + str(M))
    print("P:" + str(P))
    print("p:" + str(p))
    print("e:" + str(e))
    g = Graph(N,M)
    make_matrix_adj(p,e,P,N,M,g)
    g.dijkstra(0)

from heapq import heappop, heappush

class Grafo:
    def __init__(self, num):
        self.num = num
        self.adjacente = [[] for _ in range(num)] # Armazenar as arestas

    def inserirArestas(self, a, b, custo):
        self.adjacente[a].append((b, custo))
        self.adjacente[b].append((a, custo))

class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo

    def menorCaminho(self, org, dest):
        distancia = [float('inf')] * self.grafo.num # Distância inicial infinita
        jaVisitado = [False] * self.grafo.num
        ant = [-1] * self.grafo.num # Pegar cada vertice no caminho
        heap = [(0, org)]

        while heap:
            distAtual, a = heappop(heap)
            if jaVisitado[a]:
                continue
            jaVisitado[a] = True

            if a == dest:
                caminho = []
                b = dest
                while b != -1:  # Percorre a lista para pegar o caminho
                    caminho.append(b + 1)
                    b = ant[b]
                caminho.reverse()  # Inverter caminho
                return distancia[a], caminho

            for b, custo in self.grafo.adjacente[a]:
                if not jaVisitado[b]:
                    distNova = min(distancia[b], distAtual + custo)
                    if distNova < distancia[b]:
                        distancia[b] = distNova
                        ant[b] = a
                        heappush(heap, (distNova, b))

        return -1, []

vertices, arestas = map(int, input("Informe a quantidade de vertices e arestas do seu grafo: ").split())
grafo = Grafo(vertices)

print("Informe seu grafo: ")
for _ in range(arestas):
    a, b, custo = map(int, input().split())
    grafo.inserirArestas(a - 1, b - 1, custo)

od = input("Informe qual a origem e qual o destino: ").split("->")
origem = int(od[0]) - 1
destino = int(od[1]) - 1

dijkstra = Dijkstra(grafo)
custo, caminho = dijkstra.menorCaminho(origem, destino)

if custo == -1:
    print("\nNão existe caminho de", origem + 1, "até", destino + 1)
else:
    print("\nMenor caminho para ir de", origem + 1, "até", destino + 1, ":")
    print("", ' -> '.join(map(str, caminho)))
    print("\nCusto:", custo)



'''Exemplo de entrada:
5 6
1 2 1
1 3 2
2 4 4
3 4 3
3 5 1
4 5 5
1->5
'''
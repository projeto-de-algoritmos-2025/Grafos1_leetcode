class Solution(object):
    def findShortestCycle(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Criando o grafo como uma lista de adjacência
        grafo = [[] for _ in range(n)]
        for u, v in edges:
            grafo[u].append(v)
            grafo[v].append(u)

        menor_ciclo = float('inf')  # Inicialmente, nenhum ciclo encontrado

        # Fazemos uma BFS a partir de cada vértice
        for inicio in range(n):
            dist = [-1] * n        # Lista de distâncias (não visitado = -1)
            pai = [-1] * n         # Lista para guardar o pai de cada nó na BFS
            dist[inicio] = 0       # A distância do nó inicial para ele mesmo é 0
            fila = [inicio]        # Usamos uma lista como fila
            frente = 0             # Índice do início da fila (simulando deque)

            while frente < len(fila):
                atual = fila[frente]
                frente += 1

                for vizinho in grafo[atual]:
                    if dist[vizinho] == -1:
                        # Vizinho ainda não foi visitado
                        dist[vizinho] = dist[atual] + 1
                        pai[vizinho] = atual
                        fila.append(vizinho)
                    elif pai[atual] != vizinho:
                        # Vizinho já foi visitado e não é o pai → ciclo detectado
                        tamanho_ciclo = dist[atual] + dist[vizinho] + 1
                        if tamanho_ciclo < menor_ciclo:
                            menor_ciclo = tamanho_ciclo

        # Se nenhum ciclo foi encontrado, retorna -1
        if menor_ciclo == float('inf'):
            return -1
        return menor_ciclo

# input pelo terminal
print("Digite o número de vértices:")
n = int(input())

print("Digite o número de arestas:")
m = int(input())

edges = []
print("Digite as arestas no formato: u v")
for _ in range(m):
    u, v = map(int, input().split())
    edges.append([u, v])

# Chamada da solução
solucao = Solution()
resultado = solucao.findShortestCycle(n, edges)

print("O menor ciclo tem comprimento:", resultado)

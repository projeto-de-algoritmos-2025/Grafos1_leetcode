
#A questão 785 trata de un desafio onde temos que verificar se um grafo é bipartido ou não. É uma questão de nível médio 


class Solution:
    def isBipartite(self, grafo):
        n = len(grafo)
        cor = [-1] * n  # -1 = ainda não colorido

        for inicio in range(n):
            if cor[inicio] == -1:
                fila = [inicio]
                cor[inicio] = 0  # Começa com a cor 0

                while fila:
                    no = fila.pop(0)
                    for vizinho in grafo[no]:
                        if cor[vizinho] == -1:
                            cor[vizinho] = 1 - cor[no]  # Cor oposta
                            fila.append(vizinho)
                        elif cor[vizinho] == cor[no]:
                            # Conflito: dois nós conectados têm a mesma cor
                            return False
        return True

# input pelo terminal
print("Digite o número de vértices:")
n = int(input())

print("Digite o número de arestas:")
m = int(input())

grafo = [[] for _ in range(n)]
print("Digite as arestas no formato: u v (espaço entre os números)")
for _ in range(m):
    u, v = map(int, input().split())
    grafo[u].append(v)
    grafo[v].append(u)  # Grafo não direcionado

# Verifica se o grafo é bipartido
solucao = Solution()
if solucao.isBipartite(grafo):
    print("O grafo é bipartido.")
else:
    print("O grafo NÃO é bipartido.")

# exemplo de entrada 

# Digite o número de vértices:
# 4
# Digite o número de arestas:
# 4
# Digite as arestas no formato: u v (espaço entre os números)
# 0 1
# 1 2
# 2 3
# 3 0


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

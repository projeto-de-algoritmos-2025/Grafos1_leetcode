from collections import deque
import ast

class Solucao:
    def menorCaminhoQueVisitaTodosOsNos(self, grafo: list[list[int]]) -> int:
        n = len(grafo)
        todos_visitados = (1 << n) - 1

        fila = deque()
        visitados = set()

        for i in range(n):
            no_inicial = i
            mascara_inicial = 1 << no_inicial
            distancia_inicial = 0

            fila.append((no_inicial, mascara_inicial, distancia_inicial))
            visitados.add((no_inicial, mascara_inicial))

        while fila:
            no_atual, mascara_atual, distancia_atual = fila.popleft()

            if mascara_atual == todos_visitados:
                return distancia_atual

            for vizinho in grafo[no_atual]:
                proximo_bit = 1 << vizinho
                proxima_mascara = mascara_atual | proximo_bit
                estado = (vizinho, proxima_mascara)

                if estado not in visitados:
                    visitados.add(estado)
                    fila.append((vizinho, proxima_mascara, distancia_atual + 1))

        return -1

def executar():
    entrada = input("Digite o grafo como lista de adjacência (ex: [[1,2,3],[0],[0],[0]]): ")
    grafo = ast.literal_eval(entrada)

    solucao = Solucao()
    resposta = solucao.menorCaminhoQueVisitaTodosOsNos(grafo)

    print(f"\nMenor caminho que visita todos os nós: {resposta}")

if __name__ == "__main__":
    executar()

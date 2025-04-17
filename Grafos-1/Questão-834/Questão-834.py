from collections import defaultdict
import ast

class Solucao:
    def somaDasDistanciasNaArvore(self, n: int, arestas: list) -> list:
        arvore = defaultdict(list)
        for u, v in arestas:
            arvore[u].append(v)
            arvore[v].append(u)

        resultado = [0] * n
        contador = [1] * n

        def pos_ordem(no, pai):
            for vizinho in arvore[no]:
                if vizinho != pai:
                    pos_ordem(vizinho, no)
                    contador[no] += contador[vizinho]
                    resultado[no] += resultado[vizinho] + contador[vizinho]

        def pre_ordem(no, pai):
            for vizinho in arvore[no]:
                if vizinho != pai:
                    resultado[vizinho] = resultado[no] - contador[vizinho] + (n - contador[vizinho])
                    pre_ordem(vizinho, no)

        pos_ordem(0, -1)
        pre_ordem(0, -1)
        return resultado

def executar():
    n = int(input("n = "))
    bordas = input("bordas = ")
    arestas = ast.literal_eval(bordas)

    solucao = Solucao()
    resposta = solucao.somaDasDistanciasNaArvore(n, arestas)

    print("\nSoma das distâncias para cada nó:")
    print(resposta)

if __name__ == "__main__":
    executar()

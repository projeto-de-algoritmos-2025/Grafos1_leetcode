class No:
    def __init__(self, valor, vizinhos=None):
        self.val = valor
        self.vizinhos = vizinhos if vizinhos is not None else []

class Solucao:
    def clonarGrafo(self, no: 'No') -> 'No':
        if not no:
            return None

        visitados = {}

        def dfs(atual):
            if atual in visitados:
                return visitados[atual]

            clone = No(atual.val)
            visitados[atual] = clone

            for vizinho in atual.vizinhos:
                clone.vizinhos.append(dfs(vizinho))

            return clone

        return dfs(no)

def construir_grafo(lista_adj):
    if not lista_adj:
        return None

    nos = {i + 1: No(i + 1) for i in range(len(lista_adj))}

    for i, vizinhos in enumerate(lista_adj):
        nos[i + 1].vizinhos = [nos[v] for v in vizinhos]

    return nos[1]

def imprimir_grafo(no, visitados=None):
    if visitados is None:
        visitados = set()

    if no in visitados:
        return

    visitados.add(no)
    print(f"Nó {no.val}: {[viz.val for viz in no.vizinhos]}")

    for viz in no.vizinhos:
        imprimir_grafo(viz, visitados)

entrada = input("Insira o grafo como lista de adjacência (ex: [[2,4],[1,3],[2,4],[1,3]]): ")
lista_adj = eval(entrada)

grafo_original = construir_grafo(lista_adj)
solucao = Solucao()
grafo_clonado = solucao.clonarGrafo(grafo_original)

print("\nGrafo clonado:")
imprimir_grafo(grafo_clonado)

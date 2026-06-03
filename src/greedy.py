import heapq


def dijkstra(grafo, origem, destino):
    """
    Executa o algoritmo de Dijkstra para encontrar
    o caminho de menor custo entre dois vértices.
    """

    distancias = {v: float("inf") for v in grafo}
    predecessores = {v: None for v in grafo}

    distancias[origem] = 0

    heap = [(0, origem)]
    visitados = set()
    operacoes = 0

    while heap:
        custo_atual, atual = heapq.heappop(heap)

        if atual in visitados:
            continue

        visitados.add(atual)

        if atual == destino:
            break

        for vizinho, peso in grafo.get(atual, []):
            operacoes += 1
            novo_custo = custo_atual + peso

            if novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo
                predecessores[vizinho] = atual
                heapq.heappush(heap, (novo_custo, vizinho))

    caminho = []
    atual = destino

    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]

    caminho.reverse()

    return {
        "caminho": caminho,
        "custo": distancias[destino],
        "operacoes": operacoes,
        "distancias": distancias,
        "predecessores": predecessores
    }
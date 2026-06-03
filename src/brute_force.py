def forca_bruta_todos_caminhos(grafo, origem, destino):
    """
    Enumera todos os caminhos possíveis entre origem e destino
    usando recursão e backtracking.
    """

    melhor_caminho = None
    melhor_custo = float("inf")
    caminhos_avaliados = 0
    chamadas_recursivas = 0

    def backtrack(atual, destino, visitados, caminho, custo):
        nonlocal melhor_caminho, melhor_custo
        nonlocal caminhos_avaliados, chamadas_recursivas

        chamadas_recursivas += 1

        if atual == destino:
            caminhos_avaliados += 1

            if custo < melhor_custo:
                melhor_custo = custo
                melhor_caminho = caminho[:]

            return

        for vizinho, peso in grafo.get(atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                caminho.append(vizinho)

                backtrack(vizinho, destino, visitados, caminho, custo + peso)

                caminho.pop()
                visitados.remove(vizinho)

    backtrack(origem, destino, {origem}, [origem], 0)

    return {
        "melhor_caminho": melhor_caminho,
        "melhor_custo": melhor_custo,
        "caminhos_avaliados": caminhos_avaliados,
        "chamadas_recursivas": chamadas_recursivas
    }
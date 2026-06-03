import time
import tracemalloc


def medir_desempenho(funcao, *args):
    """Mede tempo de execução e memória utilizada por uma função."""

    tracemalloc.start()
    inicio = time.perf_counter()

    resultado = funcao(*args)

    fim = time.perf_counter()
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "resultado": resultado,
        "tempo_ms": (fim - inicio) * 1000,
        "memoria_mb": memoria_pico / (1024 * 1024)
    }


def gerar_grafo_sintetico(n):
    """Gera um grafo sintético para testes de escalabilidade."""

    grafo_teste = {i: [] for i in range(1, n + 1)}

    for i in range(1, n):
        peso = (i * 7) % 25 + 1
        grafo_teste[i].append((i + 1, peso))
        grafo_teste[i + 1].append((i, peso))

    for i in range(1, n - 2):
        peso = (i * 11) % 40 + 5
        grafo_teste[i].append((i + 3, peso))
        grafo_teste[i + 3].append((i, peso))

    return grafo_teste
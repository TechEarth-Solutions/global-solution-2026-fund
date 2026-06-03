import matplotlib.pyplot as plt
import networkx as nx


def visualizar_grafo(grafo, municipios=None, caminho_destacado=None):
    """Visualiza o grafo e destaca o caminho informado."""

    G = nx.Graph()

    for origem, vizinhos in grafo.items():
        for destino, peso in vizinhos:
            G.add_edge(origem, destino, weight=peso)

    pos = nx.spring_layout(G, seed=42)

    labels = {}
    for node in G.nodes:
        if municipios and node in municipios:
            labels[node] = municipios[node]["nome"]
        else:
            labels[node] = str(node)

    nx.draw(G, pos, with_labels=True, labels=labels, node_size=900, font_size=8)

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    if caminho_destacado:
        arestas_caminho = list(zip(caminho_destacado, caminho_destacado[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=arestas_caminho, width=4)

    plt.title("Grafo de municípios com rota destacada")
    plt.show()
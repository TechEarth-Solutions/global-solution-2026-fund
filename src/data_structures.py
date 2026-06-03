municipios = {
    1: {"nome": "Porto Alegre", "risco": 0.72, "custo": 1850.0, "populacao": 1400000, "cenario": "RS"},
    2: {"nome": "Canoas", "risco": 0.84, "custo": 1200.0, "populacao": 350000, "cenario": "RS"},
    3: {"nome": "São Leopoldo", "risco": 0.79, "custo": 1100.0, "populacao": 240000, "cenario": "RS"},
    4: {"nome": "Novo Hamburgo", "risco": 0.68, "custo": 1300.0, "populacao": 245000, "cenario": "RS"},
    5: {"nome": "Pelotas", "risco": 0.63, "custo": 1600.0, "populacao": 330000, "cenario": "RS"},
    6: {"nome": "Balsas", "risco": 0.88, "custo": 1750.0, "populacao": 96000, "cenario": "MATOPIBA"},
    7: {"nome": "Palmas", "risco": 0.74, "custo": 1650.0, "populacao": 310000, "cenario": "MATOPIBA"},
    8: {"nome": "Barreiras", "risco": 0.81, "custo": 1500.0, "populacao": 160000, "cenario": "MATOPIBA"},
    9: {"nome": "Uruçuí", "risco": 0.91, "custo": 1400.0, "populacao": 22000, "cenario": "MATOPIBA"},
    10: {"nome": "Luís Eduardo Magalhães", "risco": 0.77, "custo": 1450.0, "populacao": 110000, "cenario": "MATOPIBA"}
}

grafo = {
    1: [(2, 15), (3, 35), (5, 260)],
    2: [(1, 15), (3, 20), (4, 45)],
    3: [(1, 35), (2, 20), (4, 25)],
    4: [(2, 45), (3, 25), (5, 240)],
    5: [(1, 260), (4, 240), (6, 700)],
    6: [(5, 700), (7, 450), (8, 300)],
    7: [(6, 450), (8, 320), (9, 280)],
    8: [(6, 300), (7, 320), (9, 210), (10, 90)],
    9: [(7, 280), (8, 210), (10, 180)],
    10: [(8, 90), (9, 180)]
}


class Node:
    """Representa um nó da Árvore Binária de Busca."""

    def __init__(self, municipio_id, dados):
        self.municipio_id = municipio_id
        self.risco = dados["risco"]
        self.dados = dados
        self.left = None
        self.right = None


class BinarySearchTree:
    """Árvore Binária de Busca para organizar municípios pelo índice de risco."""

    def __init__(self):
        self.root = None

    def inserir(self, municipio_id, dados):
        """Insere um município na BST usando o índice de risco como chave."""
        novo = Node(municipio_id, dados)

        if self.root is None:
            self.root = novo
        else:
            self._inserir_rec(self.root, novo)

    def _inserir_rec(self, atual, novo):
        if novo.risco < atual.risco:
            if atual.left is None:
                atual.left = novo
            else:
                self._inserir_rec(atual.left, novo)
        else:
            if atual.right is None:
                atual.right = novo
            else:
                self._inserir_rec(atual.right, novo)

    def buscar_intervalo(self, r_min, r_max):
        """Busca municípios com risco dentro do intervalo informado."""
        resultado = []
        self._buscar_intervalo_rec(self.root, r_min, r_max, resultado)
        return resultado

    def _buscar_intervalo_rec(self, node, r_min, r_max, resultado):
        if node is None:
            return

        if node.risco > r_min:
            self._buscar_intervalo_rec(node.left, r_min, r_max, resultado)

        if r_min <= node.risco <= r_max:
            resultado.append((node.municipio_id, node.dados["nome"], node.risco))

        if node.risco < r_max:
            self._buscar_intervalo_rec(node.right, r_min, r_max, resultado)

    def in_order(self):
        """Retorna os municípios em ordem crescente de risco."""
        resultado = []
        self._in_order_rec(self.root, resultado)
        return resultado

    def _in_order_rec(self, node, resultado):
        if node:
            self._in_order_rec(node.left, resultado)
            resultado.append((node.municipio_id, node.dados["nome"], node.risco))
            self._in_order_rec(node.right, resultado)

    def altura(self):
        """Calcula a altura da BST."""
        return self._altura_rec(self.root)

    def _altura_rec(self, node):
        if node is None:
            return 0

        return 1 + max(self._altura_rec(node.left), self._altura_rec(node.right))
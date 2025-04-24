from node import Distance

class Path:
    def __init__(self, nodes=None, cost=0):
        """Inicialitza un camí amb una llista de nodes i un cost total."""
        self.nodes = nodes if nodes is not None else []
        self.cost = cost  # Cost real acumulat

    def LastNode(self):
        """Retorna l'últim node del camí (el més recent afegit)."""
        if self.nodes:
            return self.nodes[-1]
        return None

    def ContainsNode(self, node):
        """Retorna True si el node ja és en el camí."""
        return node in self.nodes

    def CopyAndAdd(self, node, segment_cost, estimated_cost):
        """
        Retorna una còpia del camí actual amb el nou node afegit.
        Actualitza el cost acumulat i l'estimat fins a la destinació.
        """
        new_nodes = self.nodes.copy()
        new_nodes.append(node)
        new_cost = self.cost + segment_cost
        total_cost = new_cost + estimated_cost
        return Path(new_nodes, new_cost), total_cost

    def CostToNode(self, node):
        """Retorna el cost acumulat fins al node indicat. Si no hi és, retorna -1."""
        if node not in self.nodes:
            return -1
        index = self.nodes.index(node)
        cost = 0
        for i in range(index):
            cost += Distance(self.nodes[i], self.nodes[i + 1])
        return cost

def AddNodeToPath(path, node, segment_cost, estimated_cost):
    """Retorna una nova instància de Path amb el nou node afegit."""
    return path.CopyAndAdd(node, segment_cost, estimated_cost)[0]

def ContainsNode(path, node):
    """Funció externa per comprovar si un node està en el camí."""
    return path.ContainsNode(node)

def CostToNode(path, node):
    """Funció externa per obtenir el cost acumulat fins a un node dins del camí."""
    return path.CostToNode(node)

def PlotPath(graph, path):
    """Mostra gràficament el camí en el graf indicat."""
    import matplotlib.pyplot as plt

    if not path.nodes:
        return

    plt.figure(figsize=(8, 6))

    # Dibuixar segments del camí
    for i in range(len(path.nodes) - 1):
        n1 = path.nodes[i]
        n2 = path.nodes[i + 1]
        plt.plot([n1.x, n2.x], [n1.y, n2.y], 'b-', linewidth=2)
        plt.text((n1.x + n2.x) / 2, (n1.y + n2.y) / 2,
                 f'{Distance(n1, n2):.2f}', color='blue')

    # Dibuixar nodes
    for node in graph.nodes.values():
        color = 'blue' if node in path.nodes else 'gray'
        plt.scatter(node.x, node.y, color=color)
        plt.text(node.x, node.y, node.name, fontsize=12, ha='right')

    plt.title("Shortest Path")
    plt.show()
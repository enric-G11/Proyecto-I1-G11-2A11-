import matplotlib.pyplot as plt
import math

# Classe que representa un node en el graf
class Node:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = float(x)  # Convertir a float per assegurar compatibilitat
        self.y = float(y)
        self.neighbors = []

    def __repr__(self):
        return f"Node({self.name}, {self.x}, {self.y})"

# Classe que representa un segment entre dos nodes
class Segment:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.cost = math.sqrt((destination.x - origin.x) ** 2 + (destination.y - origin.y) ** 2)

    def __repr__(self):
        return f"Segment({self.origin.name} -> {self.destination.name}, Cost: {self.cost:.2f})"

# Classe que representa un graf
class Graph:
    def __init__(self):
        self.nodes = {}  # Diccionari {nom_node: Node}
        self.segments = []  # Llista de segments

    def AddNode(self, name, x=0, y=0):
        """Afegeix un node al graf si no existeix"""
        if name in self.nodes:
            return False
        self.nodes[name] = Node(name, x, y)
        return True

    def AddSegment(self, nameOriginNode, nameDestinationNode):
        """Afegeix un segment entre dos nodes existents"""
        if nameOriginNode not in self.nodes or nameDestinationNode not in self.nodes:
            return False
        origin = self.nodes[nameOriginNode]
        destination = self.nodes[nameDestinationNode]
        segment = Segment(origin, destination)
        self.segments.append(segment)

        # Afegim els nodes com a veïns
        self.AddNeighbor(origin, destination)
        self.AddNeighbor(destination, origin)
        return True

    def AddNeighbor(self, n1, n2):
        """Afegeix un veí a un node"""
        if n2 not in n1.neighbors:
            n1.neighbors.append(n2)
            return True
        return False

    def Distance(self, n1, n2):
        """Calcula la distància entre dos nodes"""
        return math.sqrt((n1.x - n2.x) ** 2 + (n1.y - n2.y) ** 2)

    def Plot(self):
        """Dibuixa el graf amb nodes i segments"""
        plt.figure(figsize=(8, 6))

        # Dibuixar segments
        for segment in self.segments:
            plt.plot([segment.origin.x, segment.destination.x],
                     [segment.origin.y, segment.destination.y], 'k-')
            plt.text((segment.origin.x + segment.destination.x) / 2,
                     (segment.origin.y + segment.destination.y) / 2,
                     f'{segment.cost:.2f}', color='red')

        # Dibuixar nodes
        for node in self.nodes.values():
            plt.scatter(node.x, node.y, color='gray')
            plt.text(node.x, node.y, node.name, fontsize=12, ha='right')

        plt.show()

    def LoadFromFile(self, filename):
        """Carrega un graf des d'un fitxer de text"""
        try:
            with open(filename, 'r') as file:
                mode = None
                for line in file:
                    line = line.strip()
                    if line == "NODES":
                        mode = "nodes"
                        continue
                    elif line == "SEGMENTS":
                        mode = "segments"
                        continue

                    parts = line.split()
                    if mode == "nodes" and len(parts) == 3:
                        name, x, y = parts[0], float(parts[1]), float(parts[2])
                        self.AddNode(name, x, y)

                    elif mode == "segments" and len(parts) == 2:
                        self.AddSegment(parts[0], parts[1])

        except FileNotFoundError:
            print(f"Error: El fitxer '{filename}' no s'ha trobat.")